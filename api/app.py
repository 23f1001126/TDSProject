from multiprocessing import Process
import subprocess
from fastapi import FastAPI, File, Form, UploadFile, HTTPException, Depends, Query, Request
from fastapi.responses import JSONResponse
import os
import json
from typing import Optional, Dict, Any, Union
import shutil
from utils.question_matching import find_similar_question
from utils.file_process import process_uploaded_file
from utils.function_definations_llm import function_definitions_objects_llm
from utils.openai_api import extract_parameters
from utils.solution_functions import functions_dict

tmp_dir = "tmp_uploads"
os.makedirs(tmp_dir, exist_ok=True)

app = FastAPI()

@app.get("/")
def fun():
    return "works"

SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")

@app.get('/redeploy')
def redeploy(password: str = Query(None)):
    if password != SECRET_PASSWORD:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return {"message": "Redeployment not available in cloud environment"}

async def save_upload_file(upload_file: UploadFile) -> str:
    """Save an uploaded file to disk and return its path"""
    UPLOAD_DIR = "tmp_uploads"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(tmp_dir, upload_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path

def convert_answer_to_string(answer: Union[str, Dict, list, Any]) -> str:
    """Convert any answer type to properly formatted string"""
    if isinstance(answer, str):
        return answer
    elif isinstance(answer, (dict, list)):
        try:
            return json.dumps(answer, ensure_ascii=False)
        except (TypeError, ValueError):
            return str(answer)
    else:
        return str(answer)


from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import json
import inspect
from typing import Optional, Dict, Any, Union
import shutil
from utils.question_matching import find_similar_question
from utils.file_process import process_uploaded_file
from utils.function_definations_llm import function_definitions_objects_llm
from utils.openai_api import extract_parameters
from utils.solution_functions import functions_dict


def filter_arguments_for_function(func, arguments: Dict) -> Dict:
    """Filter arguments to only include what the function accepts"""
    if not callable(func):
        return {}
    
    # Get the function's signature
    sig = inspect.signature(func)
    parameters = sig.parameters
    
    # Filter arguments to only include what the function accepts
    filtered_args = {
        k: v for k, v in arguments.items() 
        if k in parameters
    }
    
    # Add default values for missing but required parameters
    for param_name, param in parameters.items():
        if (param.default is inspect.Parameter.empty and 
            param_name not in filtered_args and
            param.kind != param.VAR_KEYWORD):
            filtered_args[param_name] = None  # Or appropriate default
            
    return filtered_args

@app.post("/")
async def process_file(
    question: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    file_names = []
    tmp_dir_local = tmp_dir
    file_data = {}
    

    # Handle the file processing if file is present
    matched_function = find_similar_question(question)
    function_name = matched_function[0]
    print("-----------Matched Function------------\n", function_name)
    
    if file:
        print("received file")
        file_path = await save_upload_file(file)
        try:
            tmp_dir_local, file_names = process_uploaded_file(file_path)
            file_data = {
                "file_path": os.path.join(tmp_dir_local, file_names[0]) if file_names else None,
                "original_filename": file.filename,
                "tmp_dir": tmp_dir_local
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    # Extract parameters using LLM
    parameters = extract_parameters(
        str(question),
        function_definitions_llm=function_definitions_objects_llm.get(function_name, {}),
    )
    print("-----------parameters------------\n", parameters)

    if not parameters or "arguments" not in parameters:
        raise HTTPException(
            status_code=400, 
            detail="Failed to extract parameters for the given question"
        )

    solution_function = functions_dict.get(
        function_name, 
        lambda **kwargs: json.dumps({"error": "No matching function found"})
    )

    try:
        arguments = json.loads(parameters["arguments"])
    except (TypeError, json.JSONDecodeError) as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid arguments format: {str(e)}"
        )

    # Combine all possible arguments
    combined_args = {**arguments, **file_data}
    
    # Filter arguments to only what the function accepts
    filtered_args = filter_arguments_for_function(solution_function, combined_args)
    print("-----------filtered_args------------\n", filtered_args)

    try:
        # Execute with only the needed arguments
        answer = solution_function(**filtered_args)
        answer_str = convert_answer_to_string(answer)
    except Exception as e:
        error_msg = f"Error executing function: {str(e)}"
        answer_str = json.dumps({"error": error_msg})
        raise HTTPException(status_code=500, detail=error_msg)
    finally:
        # Clean up temporary files
        
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted temporary file: {file_path}")
            except OSError as e:
                print(f"Warning: Failed to delete file {file_path}: {e}")

        
        if file_data.get("tmp_dir") and os.path.exists(file_data["tmp_dir"]):
            try:
                shutil.rmtree(file_data["tmp_dir"])
            except OSError as e:
                print(f"Warning: Failed to clean up temp directory: {e}")

    return {"answer": answer_str}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)
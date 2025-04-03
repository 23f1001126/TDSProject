import subprocess
import uvicorn
import os
import inspect
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Query
from pydantic import BaseModel
from utils.question_matching import find_similar_question
from utils.file_process import unzip_folder
from utils.function_definations_llm import function_definitions_objects_llm
from utils.openai_api import extract_parameters
from utils.solution_functions import functions_dict

# Ensure the temporary directory exists
tmp_dir = "tmp_uploads"
os.makedirs(tmp_dir, exist_ok=True)

app = FastAPI()
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")


class QuestionRequest(BaseModel):
    question: str


@app.post("/")
async def process_file(
    question: str = Form(...),
    file: UploadFile = File(None)
):
    """Handles incoming questions & optional file uploads."""
    file_path = None  # This will hold the saved file path if a file is uploaded
    file_names = []
    tmp_dir_local = "tmp_uploads"

    try:
        matched_function, matched_description = find_similar_question(question)

        if file:
            # Save the uploaded file to disk
            file_path = os.path.join(tmp_dir_local, file.filename)
            with open(file_path, "wb") as f:
                f.write(await file.read())

            # Process the file: if it's a zip, unzip_folder returns the new path; otherwise, it moves the file.
            file_path, file_names = unzip_folder(file_path)

        # Extract parameters using the matched function's definition.
        parameters = extract_parameters(
            question, function_definitions_llm=function_definitions_objects_llm[matched_function]
        )

        if parameters is None:
            print("No parameters detected, using empty list as parameters")
            parameters = []

        solution_function = functions_dict.get(
            matched_function, lambda *args, **kwargs: "No matching function found"
        )

        # Inspect the solution function's signature to determine how to pass arguments.
        sig = inspect.signature(solution_function)
        if len(sig.parameters) == 0:
            answer = solution_function()
        else:
            if file:
                if isinstance(parameters, dict):
                    answer = solution_function(file_path, **parameters)
                else:
                    answer = solution_function(file_path, *parameters)
            else:
                if isinstance(parameters, dict):
                    answer = solution_function(**parameters)
                else:
                    answer = solution_function(*parameters)

        print(answer)
        return {"answer": answer}
    except Exception as e:
        print(e, "this is the error")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/redeploy")
async def redeploy(password: str = Query(..., description="Admin password for redeployment")):
    """Triggers redeployment if the correct password is provided."""
    if password != SECRET_PASSWORD:
        raise HTTPException(status_code=403, detail="Unauthorized")

    subprocess.run(["../redeploy.sh"], shell=True)
    return {"message": "Redeployment triggered!"}


if __name__ == "__main__":
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)
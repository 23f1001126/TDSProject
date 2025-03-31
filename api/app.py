from multiprocessing import Process
import subprocess
from flask import Flask, request, jsonify
import os
import inspect
from utils.question_matching import find_similar_question
from utils.file_process import unzip_folder
from utils.function_definations_llm import function_definitions_objects_llm
from utils.openai_api import extract_parameters
from utils.solution_functions import functions_dict

from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
# Ensure the temporary directory exists
tmp_dir = "tmp_uploads"
os.makedirs(tmp_dir, exist_ok=True)

app = FastAPI()
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")


@app.route("/", methods=["POST"])
def process_file():
    question = request.form.get("question")
    file = request.files.get("file")
    file_path = None  # This will hold the saved file path if a file is uploaded
    file_names = []
    tmp_dir_local = "tmp_uploads"

    try:
        matched_function, matched_description = find_similar_question(question)

        if file:
            # Save the uploaded file to disk
            file_path = os.path.join(tmp_dir_local, file.filename)
            file.save(file_path)
            # Process the file: if it's a zip, unzip_folder returns the new path; otherwise, it moves the file.
            file_path, file_names = unzip_folder(file_path)

        # Extract parameters using the matched function's definition.
        parameters = extract_parameters(str(question),
                                        function_definitions_llm=function_definitions_objects_llm[matched_function])
        if parameters is None:
            print("No parameters detected, using empty list as parameters")
            parameters = []

        solution_function = functions_dict.get(
            str(matched_function),
            lambda *args, **kwargs: "No matching function found"
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
        return jsonify({"answer": answer})
    except Exception as e:
        print(e, "this is the error")
        return jsonify({"error": str(e)}), 500


@app.route('/redeploy', methods=['GET'])
def redeploy():
    password = request.args.get('password')
    print(password)
    print(SECRET_PASSWORD)
    if password != SECRET_PASSWORD:
        return "Unauthorized", 403
    subprocess.run(["../redeploy.sh"], shell=True)
    return "Redeployment triggered!", 200


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)
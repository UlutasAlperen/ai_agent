from google.genai import types

from functions.get_files_info import schema_get_files_info ,get_files_info
from functions.get_file_content import schema_get_file_content,get_file_content
from functions.run_python import schema_run_python_file,run_python_file
from functions.write_file_content import schema_write_file,write_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

FUNCTIONS = {
    "get_files_info":get_files_info,
    "get_file_content":get_file_content,
    "run_python_file":run_python_file,
    "write_file":write_file,
}

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    args = dict(function_call_part.args)
    args["working_directory"] = "./calculator"

    if verbose:
        print(f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in FUNCTIONS:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"}
                )
            ]
        )

    try:
        result = FUNCTIONS[function_name](**args)
    except Exception as e:
        result = f"Exception: {e}"

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result}
            )
        ]
    )


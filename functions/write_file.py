import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        full_working_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(full_working_path, file_path))

        dir_is_valid = os.path.commonpath([full_working_path, full_path]) == full_working_path
    
        if not dir_is_valid:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(full_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(full_working_path, exist_ok=True)

        with open(full_path, "w") as file:
            file_contents = file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the path relative to working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path","content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to a file for content to be written to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="A string to be written to a file"
            ),
        },
    ),
)
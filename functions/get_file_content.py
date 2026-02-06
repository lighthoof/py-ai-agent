import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        full_working_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(full_working_path, file_path))
        if not os.path.exists(full_path):
            return f'Error: "{file_path}" is not a file'

        dir_is_valid = os.path.commonpath([full_working_path, full_path]) == full_working_path
    
        if not dir_is_valid:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, "r") as file:
            file_contents = file.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if file.read(1):
                file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f'Error: {e}'
    
    return file_contents

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads a file in a directory relative to the working directory, reads a maximum of 10000 characters ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to a file to be read, relative to the working directory",
            ),
        },
    ),
)
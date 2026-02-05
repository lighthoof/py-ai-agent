import os

def get_files_info(working_directory, directory="."):
    try:
        full_working_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(full_working_path, directory))
        if not os.path.exists(full_path):
            return f'Error: "{directory}" is not a directory'

        dir_is_valid = os.path.commonpath([full_working_path, full_path]) == full_working_path
    
        if not dir_is_valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        response = ""
        for entry in os.listdir(full_path):
            filesize = os.path.getsize(os.path.join(full_path, entry))
            is_dir = os.path.isdir(os.path.join(full_path, entry))
            line = f"- {entry}: file_size={filesize}, is_dir={is_dir}\n"
            response += line
    except Exception as e:
        return f"Error: {e}"

    return response

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
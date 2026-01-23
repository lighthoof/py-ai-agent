import os
from config import MAX_CHARS
def get_file_content(working_directory, filepath):
    try:
        full_working_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(full_working_path, filepath))
        if not os.path.exists(full_path):
            return f'Error: "{filepath}" is not a file'

        dir_is_valid = os.path.commonpath([full_working_path, full_path]) == full_working_path
    
        if not dir_is_valid:
            return f'Error: Cannot list "{filepath}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{filepath}"'

        with open(full_path, "r") as file:
            file_contents = file.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if file.read(1):
                file_contents += f'[...File "{filepath}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f'Error: {e}'
    
    return file_contents
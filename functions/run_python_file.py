import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        full_working_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(full_working_path, file_path))

        dir_is_valid = os.path.commonpath([full_working_path, full_path]) == full_working_path
    
        if not dir_is_valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_path]
        if args != None:
            command.extend(args)

        process = subprocess.run(command, capture_output=True, timeout=30, text=True)

        output = ""
        if process.returncode != 0:
            output += f'Process exited with code {process.returncode}\n'

        if len(process.stderr) == 0 and len(process.stdout) == 0:
            output += f'No output produced\n'

        output += f"STDOUT: \n{process.stdout}\n"
        output += f"STDERR: \n{process.stderr}\n"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return output
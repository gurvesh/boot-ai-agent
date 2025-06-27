import os
import subprocess

def run_python_file(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    if file_path.startswith("/"):
        full_file_path = file_path
    else:
        full_file_path = os.path.abspath(working_directory + "/" + file_path)
    file_name = os.path.basename(full_file_path)
    try:
        if not full_file_path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_file_path):
            return f'Error: File "{file_path}" not found.'
        if not file_name.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        out = ''
        
        result = subprocess.run(
            ["python", "-m", f'{file_name[:-3]}'], 
            timeout=30, 
            capture_output=True, 
            cwd=os.path.dirname(full_file_path)
        )

        out += "No output produced\n" if result.stdout == b'' else f"STDOUT: {result.stdout}\n"
        out += f"STDERR: {result.stderr}\n"
        out += '' if result.returncode == 0 else f"Process exited with code {result.returncode}\n"
        return out
    except Exception as e:
        return f'Error executing Python file: {e}'
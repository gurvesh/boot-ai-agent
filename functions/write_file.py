import os

def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    if not file_path.startswith("/"):
        file_path = os.path.abspath(working_directory + "/" + file_path)
    try:
        if not file_path.startswith(working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        file_dir = os.path.dirname(file_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        with open(file_path, "w+") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
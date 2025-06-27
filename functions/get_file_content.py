import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    if not file_path.startswith("/"):
        file_path = os.path.join(working_directory, file_path)
    try:
        if not file_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f'Error: {e}'
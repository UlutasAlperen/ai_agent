import os
from . import config

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > config.MAX_FILE_LENGTH:
            truncated = content[:config.MAX_FILE_LENGTH]
            truncated += f'\n[...File "{file_path}" truncated at {config.MAX_FILE_LENGTH} characters]'
            return truncated

        return content

    except Exception as e:
        return f"Error: {e}"


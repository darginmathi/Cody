import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
    except Exception as e:
        return f"Error: creating directory: {e}"
    if os.path.exists(target_file_path) and os.path.isdir(target_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(target_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: writing file "{file_path}": {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates a new file and writes the content to it or if the file already exists it overwrites it.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is to be written.",
            ),
        },
    ),
)

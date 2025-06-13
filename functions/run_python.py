import os

def run_python(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot run "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'

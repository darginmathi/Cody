import os
import sys

def get_files_info(working_directory, directory=None):
    abs_wd = os.path.abspath(working_directory)
    if directory == None:
        abs_dir = os.path.abspath(working_directory)
    else:
        abs_dir = os.path.abspath(os.path.join(abs_wd, directory))
    if not abs_dir.startswith(abs_wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files = os.listdir(abs_dir)
    except Exception as e:
        return f"Error: {str(e)}"

    lines = []

    for file in files:
        error = ""
        file_path = os.path.join(abs_dir, file)
        try:
            file_size = os.path.getsize(file_path)
        except Exception as e:
            file_size = 0
        try:
            is_dir = os.path.isdir(file_path)
        except Exception as e:
            is_dir = False

        lines.append(f'- {file}: file_size={file_size} bytes, is_dir={is_dir}')

    return "\n".join(lines)

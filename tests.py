from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file_content import write_file


def test():
    print(get_file_content("calculator", "main.py"))
    print(write_file('calculator', 'main.txt', 'hello'))
    print(run_python_file("calculator", "main.py"))
    print(get_files_info('calculator', 'pkg'))


if __name__ == "__main__":
    test()

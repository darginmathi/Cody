from functions.get_files_info import get_files_info


def test():
    print(get_files_info({'directory': '.'}))
    print(get_files_info({'directory': 'pkg'}))


if __name__ == "__main__":
    test()

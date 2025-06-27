# tests.py

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    # # Test get_files_info:
    # print("testing: get_files_info .")
    # print(get_files_info("calculator", "."))

    # print("testing: get_files_info pkg")
    # print(get_files_info("calculator", "pkg"))

    # print("testing: get_files_info /bin")
    # print(get_files_info("calculator", "/bin"))

    # print("testing: get_files_info '../'")
    # print(get_files_info("calculator", "../"))

    # print("testing: get_files_info None")
    # print(get_files_info("calculator"))

    # Test get_file_contents:
    # print("testing: get_file_contents lorem")
    # print(get_file_content("calculator", "lorem.txt"))

    # print("testing: get_file_contents main.py")
    # print(get_file_content("calculator", "main.py"))

    # print("testing: get_file_contents pkg/calculator.py")
    # print(get_file_content("calculator", "pkg/calculator.py"))

    # print("testing: get_file_contents /bin/cat")
    # print(get_file_content("calculator", "/bin/cat"))

    # # Test write_file:
    # print("testing write: lorem.txt")
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    # print("testing write: morelorem.txt")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    # print("testing write: bounds")
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    # # Test run_file
    # print("testing run python: main.py")
    # print(run_python_file("calculator", "main.py"))

    # print("testing run tests.py for calculator")
    # print(run_python_file("calculator", "tests.py"))

    # print("testing execute outside bounds")
    # print(run_python_file("calculator", "../main.py"))

    # print("testing execute non-existent file")
    # print(run_python_file("calculator", "nonexistent.py"))
    pass

if __name__ == "__main__":
    main()
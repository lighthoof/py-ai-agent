import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_calc_man(self):
        print("Results for dispalying calculator instructions:")
        print(run_python_file("calculator", "main.py"))
    
    def test_calc_work(self):
        print("Results for using the calculator:")
        print(run_python_file("calculator", "main.py", ["3 + 5"]))

    def test_calc_tests(self):
        print("Results for running calculator tests:")
        print(run_python_file("calculator", "tests.py"))

    def test_wrong_path(self):
        print("Results for wrong path")
        print(run_python_file("calculator", "../main.py"))

    def test_path_not_exist(self):
        print("Results for nonexistent file:")
        print(run_python_file("calculator", "nonexistent.py"))

    def test_not_py(self):
        print("Results for wrong file type:")
        print(run_python_file("calculator", "lorem.txt"))
    

if __name__ == "__main__":
    unittest.main()
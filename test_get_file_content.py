import unittest
from functions.get_file_content import get_file_content



class TestGetFileContent(unittest.TestCase):
    def test_truncate(self):
        text = get_file_content("calculator","lorem.txt")
        result1 = len(text)
        result2 = text[-51:]

        self.assertEqual(result1, 10051) 
        self.assertEqual(result2, '[...File "lorem.txt" truncated at 10000 characters]')

    def test_current_dir(self):
        print(get_file_content("calculator","main.py"))
    
    def test_pkg_dir(self):
        print(get_file_content("calculator","pkg/calculator.py"))
        
    def test_bin_dir(self):
        print(get_file_content("calculator","/bin/cat"))
    
    def test_uplevel_dir(self):
        print(get_file_content("calculator","pkg/does_not_exist.py"))

if __name__ == "__main__":
    unittest.main()
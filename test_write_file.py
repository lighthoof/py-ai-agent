import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_lorem(self):
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
        
    def test_morelorem(self):
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    
    def test_temp(self):
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    unittest.main()
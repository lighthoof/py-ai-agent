import unittest
from functions.get_files_info import get_files_info



class TestGetFileInfo(unittest.TestCase):
    def test_current_dir(self):
        print("Results for current directory:")
        print(get_files_info("calculator","."))
    
    def test_pkg_dir(self):
        print("Results for 'pkg' directory:")
        print(get_files_info("calculator","pkg"))
        
    def test_bin_dir(self):
        print("Results for '/bin' directory:")
        print(get_files_info("calculator","/bin"))
    
    def test_uplevel_dir(self):
        print("Results for '../' directory:")
        print(get_files_info("calculator","../"))


if __name__ == "__main__":
    unittest.main()
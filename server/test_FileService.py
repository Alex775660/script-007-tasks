import FileService
import os
import pytest
import time

# Test suite
class TestMyServiceServer:
    def __init__(self):
        self.user_data_dir = "user\\data"
        self.user_dir = "user"
        self.hello_txt = "hello.txt"
        self.hello_txt_data = "hello"
        self.serv = FileService.ServiceServer()

        #run tests           
        self.test_change_dir()
        self.test_create_file()
        self.test_get_file_data()
        self.test_get_files()
        self.test_delete_file()

    # Test cases
    def test_change_dir(self):     
        self.serv.change_dir(self.user_data_dir)
        assert os.getcwd() == self.serv.root_dir + "\\" + self.user_data_dir
        self.serv.change_dir(self.user_dir)
        assert os.getcwd() == self.serv.root_dir + "\\" + self.user_dir

    def test_create_file(self):
        self.serv.create_file(self.hello_txt, self.hello_txt_data)
        assert os.path.isfile(os.getcwd() + "\\" + self.hello_txt)

    def test_get_file_data(self):
        file_data = self.serv.get_file_data(self.hello_txt)
        assert file_data['name'] == self.hello_txt
        assert file_data['content'] == self.hello_txt_data
        assert file_data['create_date'] == time.ctime(os.path.getctime(os.getcwd() + "\\" + self.hello_txt))
        assert file_data['edit_date'] == time.ctime(os.path.getmtime(os.getcwd() + "\\" + self.hello_txt))
        assert file_data['size'] == os.path.getsize(os.getcwd() + "\\" + self.hello_txt)

    def test_get_files(self):
        list_files = self.serv.get_files()
        assert list_files[0]['name'] == self.hello_txt

    def test_delete_file(self):
        self.serv.delete_file(self.hello_txt)
        assert not os.path.exists(os.getcwd() + "\\" + self.hello_txt)

if __name__ == '__main__':
    testClass = TestMyServiceServer()
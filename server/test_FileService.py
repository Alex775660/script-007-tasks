import FileService
import os
import pytest
import time


@pytest.fixture(scope='function')
def case_test_change_dir_explicit():
    print('case_test_change_dir_explicit: before test-case')
    yield {
        'user_data_dir': 'user\data',
        'user_data': 'user',
    }
    print('case_test_change_dir_explicit: after test-case')


@pytest.fixture(scope='function')
def case_test_create_file_explicit():
    print('case_test_create_file_explicit: before test-case')
    yield {
        'hello_txt': 'hello.txt',
        'hello_txt_data': 'hello'
    }
    print('case_test_create_file_explicit: after test-case')


@pytest.fixture(scope='function')
def case_test_get_file_data_explicit():
    print('case_test_get_file_data_explicit: before test-case')
    yield {
        'hello_txt': 'hello.txt',
        'hello_txt_data': 'hello'
    }
    print('case_test_get_file_data_explicit: after test-case')


@pytest.fixture(scope='function')
def case_test_get_files_explicit():
    print('case_test_get_files_explicit: before test-case')
    yield {
        'hello_txt': 'hello.txt',
    }
    print('case_test_get_files_explicit: after test-case')


@pytest.fixture(scope='function')
def case_test_delete_file_explicit():
    print('case_test_delete_file_explicit: before test-case')
    yield {
        'hello_txt': 'hello.txt',
    }
    print('case_test_delete_file_explicit: after test-case')


# Test suite
class TestMyFileService:

    serv = FileService.FileService()

    # Test cases
    def test_change_dir(self, case_test_change_dir_explicit):
        assert case_test_change_dir_explicit['user_data_dir'] == 'user\data'
        assert case_test_change_dir_explicit['user_data'] == 'user'

        self.serv.change_dir(case_test_change_dir_explicit['user_data_dir'])
        assert os.getcwd() == os.path.join(self.serv.root_dir, case_test_change_dir_explicit['user_data_dir'])
        self.serv.change_dir(case_test_change_dir_explicit['user_data'])
        assert os.getcwd() == os.path.join(self.serv.root_dir, case_test_change_dir_explicit['user_data'])


    def test_create_file(self, case_test_create_file_explicit):
        assert case_test_create_file_explicit['hello_txt'] == 'hello.txt'
        assert case_test_create_file_explicit['hello_txt_data'] == 'hello'

        assert os.path.exists(self.serv.root_dir)
        assert not os.path.exists(os.path.join(os.getcwd(), case_test_create_file_explicit['hello_txt']))
        self.serv.create_file(case_test_create_file_explicit['hello_txt'], case_test_create_file_explicit['hello_txt_data'])
        assert os.path.isfile(os.path.join(os.getcwd(), case_test_create_file_explicit['hello_txt']))


    def test_get_file_data(self, case_test_get_file_data_explicit):
        assert case_test_get_file_data_explicit['hello_txt'] == 'hello.txt'
        assert case_test_get_file_data_explicit['hello_txt_data'] == 'hello'

        file_data = self.serv.get_file_data(case_test_get_file_data_explicit['hello_txt'])
        assert file_data['name'] == case_test_get_file_data_explicit['hello_txt']
        assert file_data['content'] == case_test_get_file_data_explicit['hello_txt_data']
        assert file_data['create_date'] == time.ctime(os.path.getctime(os.path.join(os.getcwd(), case_test_get_file_data_explicit['hello_txt'])))
        assert file_data['edit_date'] == time.ctime(os.path.getmtime(os.path.join(os.getcwd(), case_test_get_file_data_explicit['hello_txt'])))
        assert file_data['size'] == os.path.getsize(os.path.join(os.getcwd(), case_test_get_file_data_explicit['hello_txt']))


    def test_get_files(self, case_test_get_files_explicit):
        assert case_test_get_files_explicit['hello_txt'] == 'hello.txt'

        list_files = self.serv.get_files()
        assert len(list_files) == 1
        assert list_files[len(list_files) - 1]['name'] == case_test_get_files_explicit['hello_txt']


    def test_delete_file(self, case_test_delete_file_explicit):
        assert case_test_delete_file_explicit['hello_txt'] == 'hello.txt'

        self.serv.delete_file(case_test_delete_file_explicit['hello_txt'])
        assert not os.path.exists(os.path.join(os.getcwd(), case_test_delete_file_explicit['hello_txt']))

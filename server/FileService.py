import os
import sys
import traceback
import time

class ServiceServer:
    def change_dir(self, path: str, autocreate: bool = True) -> None:
        """Change current directory of app.

        Args:
            path (str): Path to working directory with files.
            autocreate (bool): Create folder if it doesn't exist.

        Raises:
            RuntimeError: if directory does not exist and autocreate is False.
            ValueError: if path is invalid.
        """

        #pass
        try:
            if type(path) != str:
                raise TypeError(f'incorrect type: {type(path)}')
            elif not os.path.exists(self.root_dir + "\\" + path) and not autocreate:
                raise RuntimeError("Directory does not exist and autocreate is False")  # if directory does not exist and autocreate is False
            elif not os.path.exists(self.root_dir + "\\" + path) and autocreate:
                os.makedirs(self.root_dir + "\\" + path)
                os.chdir(self.root_dir + "\\" + path)
            else:
                os.chdir(self.root_dir + "\\" + path)
        except (RuntimeError, TypeError) as e:
            print(f'error occurred: {e}')
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)



    def get_files(self) -> list:
        """Get info about all files in working directory.

        Returns:
            List of dicts, which contains info about each file. Keys:
            - name (str): filename
            - create_date (datetime): date of file creation.
            - edit_date (datetime): date of last file modification.
            - size (int): size of file in bytes.
        """

        #pass
        files = []
        for file in os.listdir(os.getcwd()):
            if os.path.isfile(os.path.join(os.getcwd(), file)):
                files.append( 
                    {
                    'name': os.path.basename(file), 
                    'create_date': time.ctime(os.path.getctime(file)),
                    'edit_date': time.ctime(os.path.getmtime(file)),
                    'size': os.path.getsize(file)
                    }
                )
        return files



    def get_file_data(self, filename: str) -> dict:
        """Get full info about file.

        Args:
            filename (str): Filename.

        Returns:
            Dict, which contains full info about file. Keys:
            - name (str): filename
            - content (str): file content
            - create_date (datetime): date of file creation
            - edit_date (datetime): date of last file modification
            - size (int): size of file in bytes

        Raises:
            RuntimeError: if file does not exist.
            ValueError: if filename is invalid.
        """

        #pass
        try:
            if not os.path.normpath(filename).startswith(os.path.dirname(filename)):
                raise ValueError(f'filename is invalid: {filename}')
            elif not os.path.exists(filename):
                raise RuntimeError("file does not exist")  # if file does not exist
            else:
                return {
                    'name': filename, 
                    'content': open(filename).read(),
                    'create_date': time.ctime(os.path.getctime(filename)),
                    'edit_date': time.ctime(os.path.getmtime(filename)),
                    'size': os.path.getsize(filename)
                    }
        except (RuntimeError, ValueError) as e:
            print(f'error occurred: {e}')
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)


    def create_file(self, filename: str, content: str = None) -> dict:
        """Create a new file.

        Args:
            filename (str): Filename.
            content (str): String with file content.

        Returns:
            Dict, which contains name of created file. Keys:
            - name (str): filename
            - content (str): file content
            - create_date (datetime): date of file creation
            - size (int): size of file in bytes

        Raises:
            ValueError: if filename is invalid.
        """

        #pass
        try:
            if not os.path.normpath(filename).startswith(os.path.dirname(filename)):
                raise ValueError(f'filename is invalid: {filename}')
            elif os.path.exists(filename):
                raise RuntimeError("file already exist")  # if file already exist
            else:
                with open(filename, "w") as file:
                    file.write(content)
                    return {
                        'name': filename, 
                        'content': content,
                        'create_date': time.ctime(os.path.getctime(filename)),
                        'size': len(content)
                    }      
        except (RuntimeError, ValueError) as e:
            print(f'error occurred: {e}')
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)


    def delete_file(self, filename: str) -> None:
        """Delete file.

        Args:
            filename (str): filename

        Raises:
            RuntimeError: if file does not exist.
            ValueError: if filename is invalid.
        """

        #pass
        try:
            if not os.path.normpath(filename).startswith(os.path.dirname(filename)):
                raise ValueError(f'filename is invalid: {filename}')
            elif not os.path.exists(filename):
                raise RuntimeError("file does not exist")  # if file does not exist
            else:
                os.remove(filename)
        except (RuntimeError, ValueError) as e:
            print(f'error occurred: {e}')
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)

    def __init__(self):
        os.chdir(os.path.dirname(__file__) + "\\..\\root_dir")  #set root_dir
        self.root_dir = os.getcwd()
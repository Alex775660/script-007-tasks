import os

def filename_is_invalid(filename: str) -> None:
    """Check that filename is invalid..

    Args:
        filename (str): filename

        Raises:
            ValueError: if filename is invalid

    """

    if not os.path.normpath(filename).startswith(os.path.dirname(filename)):
        raise ValueError(f'filename is invalid: {filename}')

def file_does_not_exist(filename: str) -> None:
    """Check that filename is invalid..

    Args:
        filename (str): filename

        Raises:
            RuntimeError: if file does not exist.

    """

    if not os.path.exists(filename):
        raise RuntimeError("file does not exist")


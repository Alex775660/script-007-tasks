import logging
import json
import os
from logging.config import dictConfig

class LoggerInstance:

    def print_error(self, message: str) -> None:
        """Print error message by logger.

        Args:
            message (str): message

        """

        self.logger.error(message)


    def print_warning(self, message: str) -> None:
        """Print warning message by logger.

        Args:
            message (str): message

        """

        self.logger.warning(message)


    def print_info(self, message: str) -> None:
        """Print info message by logger.

        Args:
            message (str): message

        """

        self.logger.info(message)


    def print_debug(self, message: str) -> None:
        """Print debug message by logger.

        Args:
            message (str): message

        """

        self.logger.debug(message)



    def __init__(self, settings_path: str = os.path.dirname(__file__) + '/logger_default_settings.json') -> None:
        """Init logger.

        Args:
            settings_path (str): logger settings path

        """

        with open(settings_path) as settings_file:
            settings_data = json.load(settings_file)
            dictConfig(settings_data)
            self.logger = logging.getLogger()
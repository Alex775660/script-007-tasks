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



    def __init__(self, logger_settings: str | dict = os.path.dirname(__file__) + '/logger_default_settings.json') -> None:
        """Init logger.

        Args:
            logger_settings (str | dict): logger settings path to json file or logger settings json dictionary

        """

        if type(logger_settings) is str:
            with open(logger_settings) as settings_file:
                settings_data = json.load(settings_file)
                dictConfig(settings_data)
                self.logger = logging.getLogger()
        if type(logger_settings) is dict:
                dictConfig(logger_settings)
                self.logger = logging.getLogger()
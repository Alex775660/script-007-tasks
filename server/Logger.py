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



    def __init__(self, logger_settings: dict) -> None:
        """Init logger.

        Args:
            logger_settings (str | dict): logger settings path to json file or logger settings json dictionary

        Raises:
            TypeError: if logger_settings isn't a dictionary (JSON).

        """

        if type(logger_settings) is dict:
            dictConfig(logger_settings)
            self.logger = logging.getLogger()
        else:
            raise TypeError("logger_settings isn't a dictionary (JSON)")

import json
import os
import argparse

class ConfigParser:

    config_json = {
        "user_settings": {
        },
        "logger_settings": {
        }
    }

    def parse_config_from_CLI(self, args: argparse.Namespace)-> None:
        """Parse program configurations from Command Line.

        Args:
            args (argparse.Namespace): CLI arguments

        """

        if args.dir:
            self.config_json["user_settings"]["user_directory"] = args.dir
        if args.logger_settings:
            with open(args.logger_settings) as logger_settings_file:
                self.config_json["logger_settings"] = json.load(logger_settings_file)


    def parse_config_from_ENV(self)-> None:
        """Parse program configurations from Program + System Enviromment.

        """

        if "USER_DIRECTORY" == os.environ:
            self.config_json["user_settings"]["user_directory"] = os.environ['USER_DIRECTORY']
        if "LOGGER_SETTINGS_FILE" == os.environ:
            with open(os.environ['LOGGER_SETTINGS_FILE']) as logger_settings_file:
                self.config_json["logger_settings"] = json.load(logger_settings_file)


    def parse_config_from_default_JSON(self)-> None:
        """Parse program configurations from JSON Default Settings file.

        """

        with open(os.path.dirname(__file__) + "/../default_settings.json") as settings_file:
            all_settings = json.load(settings_file)
            self.config_json["user_settings"] = all_settings["user_settings"]
            self.config_json["logger_settings"] = all_settings["logger_settings"]

    def __init__(self, args: argparse.Namespace)-> None:
        """Parse program configurations from ENV, JSON, CLI.

        Args:
            args (argparse.Namespace): CLI arguments

        """

        self.parse_config_from_ENV()
        self.parse_config_from_default_JSON()
        self.parse_config_from_CLI(args)
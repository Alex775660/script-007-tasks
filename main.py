#!/usr/bin/env python3
import server.FileService as FileService
import server.Logger as Logger
import server.Config as Config
import argparse


def main():
    """Command line parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        help="Start User's directory name",
    )
    parser.add_argument(
        '--logger-settings',
        type=str,
        help="Path to logger's settings file",
    )
    args = parser.parse_args()

    config_parser = Config.ConfigParser()
    config_parser.parse_config_from_ENV()
    config_parser.parse_config_from_default_JSON()
    config_parser.parse_config_from_CLI(args)

    logger = Logger.LoggerInstance(config_parser.config_json["logger_settings"])

    logger.print_debug("Start File Service")
    serv = FileService.FileService()

    logger.print_debug(f'Change directory to "{config_parser.config_json["user_settings"]["user_directory"]}"')
    serv.change_dir(config_parser.config_json["user_settings"]["user_directory"])

if __name__ == '__main__':
    main()

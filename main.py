#!/usr/bin/env python3
import server.FileService as FileService
import server.Logger as Logger
import server.Config as Config
import server.WebHandler as WebHandler
import argparse

from aiohttp import web


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
    config_parser = Config.ConfigParser(args)

    # logger
    logger = Logger.LoggerInstance(config_parser.config_json["logger_settings"])

    # web service
    logger.print_debug("Start File Service")
    handler = WebHandler.WebHandler(config_parser.config_json["user_settings"]["user_directory"])
    logger.print_debug(f'Directory changed to "{config_parser.config_json["user_settings"]["user_directory"]}"')

    app = web.Application()
    app.add_routes(
        [
            web.post('/change_dir/', handler.change_dir),
            web.get('/get_files/', handler.get_files),
            web.get('/get_file_data/', handler.get_file_data),
            web.post('/create_file/', handler.create_file),
            web.get('/delete_file/', handler.delete_file)
        ]
    )
    web.run_app(app, host=config_parser.config_json["user_settings"]["host"], port=config_parser.config_json["user_settings"]["port"])

if __name__ == '__main__':
    main()

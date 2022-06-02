#!/usr/bin/env python3
import server.FileService as FileService
import argparse
import os
import server.Logger as Logger

def main():
    """Command line parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        default="",
        help='Start User\'s directory name',
    )
    parser.add_argument(
        '-logset',
        '--logger-settings',
        type=str,
        default=os.path.dirname(__file__) + "/server/logger_default_settings.json",
        help='Path to logger\'s settings file',
    )
    params = parser.parse_args()

    logger = Logger.LoggerInstance(params.logger_settings)

    logger.print_debug("Start File Service")
    serv = FileService.FileService()

    if(params.dir != ""):
        logger.print_debug(f'Change directory to "{params.dir}"')
        serv.change_dir(params.dir)

if __name__ == '__main__':
    main()

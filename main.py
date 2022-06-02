#!/usr/bin/env python3
import server.FileService as FileService
import argparse

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
    params = parser.parse_args()
    serv = FileService.FileService()
    if(params.dir != ""): serv.change_dir(params.dir)

if __name__ == '__main__':
    main()


import server.FileService as FileService
import argparse
import os
#!/usr/bin/env python3
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
    serv = FileService.ServiceServer()
    if(params.dir != ""): serv.change_dir(params.dir)

if __name__ == '__main__':
    main()

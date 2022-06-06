import json
from logging import raiseExceptions

from aiohttp import web
from pyparsing import empty

import server.FileService as FileService


class WebHandler:

    SUCCESS = {
        "status_code": 200,
        "status_message": "OK"
    }

    ERROR = {
        "status_code": 404,
        "status_message": "Not Found"
    }

    """aiohttp handler with coroutines."""

    def __init__(self, dir_from_config: str) -> None:
        self.FileService = FileService.FileService()
        self.FileService.change_dir(dir_from_config)

    async def handle(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Basic coroutine for connection testing.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with status.
        """

        return web.json_response(self.SUCCESS)

    async def change_dir(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for changing working directory with files.

        Args:
            request (Request): aiohttp request, contains JSON in body. JSON format:
            {
                "path": "string. Directory path. Required",
            }.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """

        payload = ''
        stream = request.content
        while not stream.at_eof():
            line = await stream.read()
            payload += line.decode()
        # get json
        data = json.load(payload)
        # get dir_path field
        dir_path = data.get('path')  # None by default

        if dir_path is None:
            raise web.HTTPBadRequest(body='400 HTTP error')
        else:
            return web.json_response(self.SUCCESS)


    async def get_files(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for getting info about all files in working directory.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with success status and data or error status and error message.
        """

        data = json.dumps(self.FileService.get_files())
        if data is empty:
            return web.json_response(self.ERROR)
        else:
            return web.json_response(data)


    async def get_file_data(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for getting full info about file in working directory.

        Args:
            request (Request): aiohttp request, contains filename.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """

        # http://127.0.0.1/?filename="text.txt"
        params = request.rel_url.query
        if 'filename' in params['filename']:
            filename = params['filename']

            data = json.dumps(self.FileService.get_file_data(filename))
            if data is empty:
                return web.json_response(self.ERROR)
            else:
                return web.json_response(data + self.SUCCESS)
        else:
            raise web.HTTPBadRequest(body='400 HTTP error')


    async def create_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for creating file.

        Args:
            request (Request): aiohttp request, contains JSON in body. JSON format:
            {
                'filename': 'string. filename',
                'content': 'string. Content string. Optional',
            }.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """

        payload = ''
        stream = request.content
        while not stream.at_eof():
            line = await stream.read()
            payload += line.decode()
        # get json
        data = json.load(payload)
        # get filename field
        filename = data.get('filename')  # None by default
        content = data.get('content')    # None by default

        if filename is None or content is None:
            raise web.HTTPBadRequest(body='400 HTTP error')
        else:
            return web.json_response(json.dumps(self.FileService.create_file(filename, content)) + self.SUCCESS)


    async def delete_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for deleting file.

        Args:
            request (Request): aiohttp request, contains filename.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.

        """

        # http://127.0.0.1/?filename="text.txt"
        params = request.rel_url.query
        if 'filename' in params['filename']:
            filename = params['filename']

            data = self.FileService.delete_file(filename)
            return web.json_response(data + self.SUCCESS)
        else:
            raise web.HTTPBadRequest(body='400 HTTP error')
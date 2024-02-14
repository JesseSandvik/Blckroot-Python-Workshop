#!/usr/bin/python3

import requests

from requests import Response


class HttpService:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, parameters: str) -> Response:
        response: Response = requests.get(f'{self.base_url}/{parameters}')

        if response.status_code == 200:
            return response
        else:
            raise Exception('Failed to fetch data')


#!/usr/bin/env python3

import requests_mock
from http_service import HttpService


with requests_mock.Mocker() as mocker:
    base_url: str = 'https://test.com'
    parameters: str = 'pages/1234567'
    mocker.get('https://test.com/pages/1234567', text='this is a full response')
    http_service = HttpService(base_url)
    response = http_service.get(parameters)
    print(response.status_code)
    print(response.text)

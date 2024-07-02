import re
import requests
import json_validation
import configurartion

class Send_Request:
    def __init__(self, endpoint, body):
        self.endpoint = endpoint
        self.body = body

    def check_post_request(self):
        response = requests.post(self.endpoint, json=self.body)
        response_body = response.json()
        if json_validation.validate_json(response_body):
            status_code = response.status_code
            assert int(status_code) in range(200, 300)
            configurartion.logger(f'Response status code is {status_code}')
            
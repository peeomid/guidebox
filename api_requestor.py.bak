from __future__ import unicode_literals

import requests

import guidebox
from guidebox import error
from guidebox.version import VERSION

class APIRequestor(object):
    def __init__(self, key=None):
        self.api_key = key or guidebox.api_key

    def parse_response(self, resp):
        if resp.status_code == 504:
            raise error.APIConnectionError(resp.content or resp.reason, # pragma: no cover
                resp.content, resp.status_code, resp)

        payload = resp.json()

        if resp.status_code == 200:
            return payload
        elif resp.status_code == 401:
            raise error.AuthenticationError(payload['error'],
                resp.content, resp.status_code, resp)
        elif resp.status_code in [404, 422]:
            raise error.InvalidRequestError(payload['error'],
                resp.content, resp.status_code, resp)
        else: # pragma: no cover
            raise error.APIError(payload['error'], resp.content, resp.status_code, resp)


    def request(self, method, url, params=None):
        headers = {
            'User-Agent': 'guidebox/v2 PythonBindings/%s' % VERSION
        }

        if hasattr(guidebox, 'api_version'):
            headers['Guidebox-Version'] = guidebox.api_version

        if hasattr(guidebox, 'region'):
            headers['Guidebox-Region'] = guidebox.region
        else:
            headers['Guidebox-Region'] = 'US'

        if method == 'get':
            params['api_key'] = self.api_key
            return self.parse_response(
                requests.get(guidebox.api_base + url, auth='', params=params, headers=headers)
            )


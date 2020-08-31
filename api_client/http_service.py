import requests as api
import json
import pytest


class HTTPService:
    HEADERS = {'Content-Type': "application/json; charset=UTF-8"}

    def __init__(self):
        pass

    @classmethod
    def get(cls, link, params=None):
        return cls._execute("GET", link=link, params=params)

    @classmethod
    def post(cls, link, payload=None, params=None):
        return cls._execute("POST", link=link, payload=payload, params=params)

    @classmethod
    def put(cls, link, payload, params=None):
        return cls._execute("PUT", link=link, payload=payload, params=params)

    @classmethod
    def delete(cls, link, params=None):
        return cls._execute("DELETE", link=link, params=params)

    @classmethod
    def _execute(cls, method, link, payload='', params=None):
        full_headers = dict(cls.HEADERS.items())
        print('HTTP ' + method + " " + link)
        print('    headers:\n' + json.dumps(full_headers, indent=2, sort_keys=True))
        print('____________PARAMS: _______________')
        print(params)
        response = {
            'status_code': 0,
            'content': ''
        }

        if method == "GET":
            response = api.get(url=link, headers=full_headers, params=params)
        elif method == "POST":
            if payload:
                response = api.post(url=link, json=payload, headers=full_headers, params=params)
            else:
                response = api.post(url=link, headers=full_headers, params=params)
        elif method == "PUT":
            if type(payload) == dict:
                response = api.put(url=link, json=payload, headers=full_headers, params=params)
            else:
                response = api.put(url=link, data=payload, headers=full_headers, params=params)
        elif method == "DELETE":
            response = api.delete(url=link, headers=full_headers, params=params)
        else:
            __tracebackhide__ = True
            pytest.fail("Unknown HTTP method {} used".format(method))

        if payload:
            print('    payload:' + str(payload))

        print('     status:' + str(response.status_code))

        returner = {
            'response': response,
            'is_successful': response.status_code == 200,
            'code': response.status_code
        }

        try:
            get_json = json.loads(response.content)
            returner['data'] = get_json
            if len(response.content) < 530:
                print('    content:\n' + json.dumps(get_json, indent=2, sort_keys=True))
            else:
                print('    content: ==long content==')
        except ValueError:
            returner['data'] = response.content
            if len(response.content) < 530:
                print('    content:\n' + response.content)
            else:
                print('    content: ==long content==')

        return returner

import os
from pycgilib.request import Request

test_envs = {
    "REQUEST_METHOD": "POST",
    "REMOTE_USER": "User",
    "QUERY_STRING": "key1=val1&key2=val2",
    "DOMAIN": "domain.com",
    "SCRIPT_NAME": "/app/scriptname.py",
    "SSL_PROTOCOL": "true",
}

for k, v in test_envs.items():
    os.environ[k] = v


class TestRequest:
    def test_get_query_param(self):
        request = Request(os.environ)
        param1 = request.get_param(name="key1")
        param2 = request.get_param("key2")
        assert param1 == "val1" and param2 == "val2"

    def test_get_script_path(self):
        request = Request(os.environ)
        script_path = request.get_script_path()
        assert script_path == "https://domain.com/app" 

    ## TODO: create test for getting body

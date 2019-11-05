"""
Created on Nov 05, 2019
@author: Kuznetsov Maxim <lol8funny@gmail.com>
"""

from pycgilib.response import Response


class TestResponse:
    def test_build_default_response(self):
        response = Response()

        assert response.body == b""
        assert response.status == "200 OK"
        assert response.headers == {"Content-Type": "text/plain"}

    def test_build_custom_response(self):
        response = Response(body="string", status="201 Created")
        assert (
            response.__str__()
            == "Status: 201 Created\r\nContent-Type: 'text/plain'\r\n\r\nstring"
        )

"""
Created on Nov 05, 2019
@author: Kuznetsov Maxim <lol8funny@gmail.com>
"""

import sys

"""
Default CGI response class.

You can set all response parameters in dict, passing in 
constructor, or set each parameter by setter. All unsetted params
will be set by default.
"""

# TODO: create headers getters
class Response:
    def __init__(self, body=None, content_type=None, status=None, headers=None):
        if body is None:
            self._body = b""
        else:
            self._body = body

        if status is None:
            self._status = "200 OK"
        else:
            self._status = status

        if headers is None:
            self._headers = []
        else:
            self._headers = headers

        if content_type is None:
            self._headers.append(("Content-Type", "text/plain"))
        else:
            self._headers.append(("Content-Type", content_type))

    def _body__get(self):
        return self._body

    def _body__set(self, body):
        self._body = body

    body = property(_body__get, _body__set)

    def _status__get(self):
        return self._status

    def _status__set(self, status):
        self._status = status

    status = property(_status__get, _status__set)

    def _headers__get(self):
        headers_dict = self._headers_as_dict(self._headers)
        return headers_dict

    def _headers__set(self, header):
        self._headers.append(header)

    def _headers_as_dict(self, headerslist):
        def iterate():
            for s in headerslist:
                yield s[0], s[1]

        return {k: v for k, v in iterate()}

    headers = property(_headers__get, _headers__set)

    def __str__(self):
        parts = ["Status: " + self.status]

        parts += ("{!s}: {!r}".format(k, v) for (k, v) in self.headers.items())

        parts += ["", self.body]

        return "\r\n".join(parts)

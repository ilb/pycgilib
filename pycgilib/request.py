import os
import sys
from urllib.parse import parse_qs

"""
Created on Nov 01, 2019 
@author: Kuznetsov Maxim <lol8funny@gmail.com>
"""

# TODO: add getters for all CGI environment variables
class Request:

    """
    Takes given list with environment variables,
    additional parameters from kwargs, and merges
    it on current object attributes.
    """

    def __init__(self, environ, **kwargs):
        attrs = self.__dict__
        attrs["environ"] = environ

        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def method(self):
        return self.environ.get("REQUEST_METHOD")

    @property
    def remote_user(self):
        return self.environ.get("REMOTE_USER")

    """ 
    Returns posted data from request in byte form. 
    """

    @property
    def body(self):
        content_len = self.environ.get("CONTENT_LENGHT")
        return sys.stdin.read(int(content_len))

    def get_param(self, name):
        query_string = self.environ.get("QUERY_STRING")
        parsed_query = parse_qs(query_string)
        return parsed_query.get(name, [""])[0]

    """
    Returns script path with application name, 
    but without script name. Example: http://domain.com/app
    If script placed right away after domain, returns 
    just domain.
    """

    def get_script_path(self):
        env = self.environ
        domain = env.get("DOMAIN")
        script_name = env.get("SCRIPT_NAME")
        app_name = script_name.rsplit("/", 1)[0] if "/" in script_name else ""
        return "%s://%s%s" % (self._get_scheme(), domain, app_name)

    def _get_scheme(self):
        return ("http", "https")[self.environ.get("SSL_PROTOCOL") is not None]

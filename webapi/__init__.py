# encoding: utf-8


class WebAPI(object):
    def __init__(self, url: str, username: str = '', password: str = ''):
        self._url = url
        self._username = username
        self._password = password

    @property
    def url(self) -> str:
        return self._url

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

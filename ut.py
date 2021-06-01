#!/usr/bin/python3
# -*- coding:utf-8 -*-

DEFAULT_PRG_NAME = 'pythonic-bf'
DEFAULT_VERSION = '0601.00'
DEFAULT_AUTHOR = 'nonD'
RESOLUTION = (1024, 768)
INIT_WINDOW_POS = (125, 75)


class TitleInfo:

    def __init__(
            self,
            name=DEFAULT_PRG_NAME,
            ver=DEFAULT_VERSION,
            author=DEFAULT_AUTHOR,
            title_override=None
    ):
        self.title = ''
        if title_override is None:
            self.title = '{} v.{} by {}'.format(name, ver, author)
        else:
            self.title = title_override

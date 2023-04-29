#!/usr/bin/python3
# -*- coding:utf-8 -*-
import re
from config import*


def input_file(filename: str = 'code.txt') -> tuple[str, str]:
    with open(filename, mode='r', encoding='utf8') as infile:
        s = infile.read()
        fit_chars = '+-[]<>.,'
        s_cut = ''.join(re.findall(fit_chars, s))
    return s, s_cut


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
            self.title = '{} ver {} by {}'.format(name, ver, author)
        else:
            self.title = title_override


class MemoryStrip:

    def __init__(
            self,
            length: int = STRIP_LENGTH
    ):
        self.length = length
        self.pos = 0
        self.strip = []
        for i in range(self.length):
            self.strip.append(0)

    def add(self, operand: int = 0):
        self.strip[self.pos] = (self.strip[self.pos] + operand) % MEM_MAX_VALUE

    def sub(self, operand: int = 0):
        self.add(-operand)

    def inc(self):
        self.add(1)

    def dec(self):
        self.add(-1)

    def move(self, operand: int = 0):
        self.pos = (self.pos + operand) % self.length

    def left(self, operand: int = 0):
        self.move(-operand)

    def right(self, operand: int = 0):
        self.move(operand)

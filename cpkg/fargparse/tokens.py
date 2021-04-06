"""
@copyright Copyright (c) 2021 Shamus_Rezol <shamus.rezol@mail.ru>. All rights reserved.
MIT License
"""
from .token import FToken

class FTWhitespaces(FToken, type="whitespaces"):

    @staticmethod
    def can_parse(parser):
        return (parser.char.isspace())

    @classmethod
    def parse(cls, parser):
        def _():
            return parser.char.isspace()
        parser.parse_by_condition(_)
        return None

class FTParam(FToken, type="param"):

    def __str__(self):
        return self.T + ":" + self.value

    @staticmethod
    def can_parse(parser):
        return (parser.char in "'\"" or parser.char.isalnum())

    @classmethod
    def parse(cls, parser):
        value = str()
        if parser.char in "'\"":
            pair = parser.char
            parser.advance()
            def _():
                return (parser.char != pair)
            value = parser.parse_by_condition(_)
            parser.eat(pair)
        else:
            value = parser.parse_keyword()
        return cls(value)

class FTBigFlag(FToken, type="big-flag"):

    def __str__(self):
        return self.T + ":" + self.value

    @staticmethod
    def can_parse(parser):
        return (parser.char == '-' and parser.peek() == '-')

    @classmethod
    def parse(cls, parser):
        parser.eat('--')
        key = parser.parse_keyword()
        return cls(key)

class FTFlag(FToken, type="flag"):

    def __str__(self):
        return self.T + ":" + self.value

    @staticmethod
    def can_parse(parser):
        return (parser.char == '-')

    @classmethod
    def parse(cls, parser):
        parser.eat('-')
        key = parser.parse_keyword()
        return cls(key)

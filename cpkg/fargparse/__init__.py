"""@package fargparse
@copyright Copyright (c) 2021 Shamus_Rezol <shamus.rezol@mail.ru>. All rights reserved.
MIT License
"""
from .parser import FParser

import os

def GetArgsStr():
    result = str()
    for arg in os.sys.argv:
        if ' ' in arg:
            result += "'" + arg + "'"
        else:
            result += arg
        result += ' '
    return result.rstrip(' ')

def main():
    arguments = GetArgsStr()
    print("Command line: \"" + arguments + "\"")
    parser = FParser(arguments)
    print(parser.result)

if __name__ == "__main__":
    main()

def GetArguments():
    return FParser(GetArgsStr()).result
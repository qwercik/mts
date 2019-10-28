#!/usr/bin/env python3

import re
import sys
import string
import lexer

def translateRpnToInfix(rpnFormula):
    tokens = lexer.tokenizeRpn(rpnFormula)

    stack = []
    infixFormula = ''

    for token in tokens:
        print(token)

    return infixFormula

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()
        try:
            print(translateRpnToInfix(rpnFormula))
        except IncorrectTokenError as error:
            print('Incorrect token', error)

if __name__ == '__main__':
    main()

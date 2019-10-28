#!/usr/bin/env python3

import re
import sys
import string
from tokens import tokensDescription

class IncorrectTokenError(Exception):
    pass

def parseRpn(rpnFormula):
    parsedOutput = []

    tokens = rpnFormula.split()
    for token in tokens:
        for tokenType, regex in tokensDescription.items():
            matchResult = re.match(regex, token)
            if matchResult:
                print(token, tokenType)
                break
        else:
            raise IncorrectTokenError(token)

    return ''

def translateRpnToInfix(rpnFormula):
    parsed = parseRpn(rpnFormula)
    return ''

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()
        print(translateRpnToInfix(rpnFormula))

if __name__ == '__main__':
    main()

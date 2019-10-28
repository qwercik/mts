#!/usr/bin/env python3

import re
import sys
import string
from tokens import tokensDescription

class IncorrectTokenError(Exception):
    pass

def parseRpn(rpnFormula):
    tokens = rpnFormula.split()
    for token in tokens:
        matched = None
        for tokenType, tokenDescription in tokensDescription.items():
            matchResult = re.match(tokenDescription['regex'], token)
            if matchResult:
                matched = tokenType
                break

        if not matched:
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

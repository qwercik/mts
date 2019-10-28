#!/usr/bin/env python3

import re
import sys
import string
from tokens import tokensTypes

class IncorrectTokenError(Exception):
    pass

def parseRpn(rpnFormula):
    parsedOutput = []

    tokens = rpnFormula.split()
    for token in tokens:
        for tokenType, regex in tokensTypes.items():
            matchResult = re.findall(regex, token)
            if matchResult:
                parsedOutput.append({ 'type': tokenType, 'data': matchResult[0] })
                break
        else:
            raise IncorrectTokenError(token)

    return parsedOutput

def translateRpnToInfix(rpnFormula):
    parsed = parseRpn(rpnFormula)
    print(parsed)
    return ''

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()
        try:
            print(translateRpnToInfix(rpnFormula))
        except IncorrectTokenError as error:
            print('Incorrect token', error)

if __name__ == '__main__':
    main()

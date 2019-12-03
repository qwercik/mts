#!/usr/bin/env python3

import re
import sys
import string
import lexer
import debug
import exitcodes
import translator

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()

        try:
            infixFormula = translator.translateRpnToInfix(rpnFormula)
            print(infixFormula)
        except lexer.IncorrectSymbolError as symbol:
            debug.error('Incorrect symbol ' + str(symbol), exitcodes.EXIT_INCORRECT_SYMBOL)
        except IncorrectFormulaError as formula:
            debug.error('Incorrect formula ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except:
            debug.error('Unknown error. Report the developer', exitcodes.EXIT_UNKNOWN_ERROR)

if __name__ == '__main__':
    main()

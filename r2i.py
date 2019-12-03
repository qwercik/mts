#!/usr/bin/env python3

import re
import sys
import string
import lexer
import debug
import exitcodes
import translator

DEVELOPER_URL = 'https://github.com/qwercik/r2i'

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()

        try:
            infixFormula = translator.translateRpnToInfix(rpnFormula)
            print(infixFormula)
        except lexer.IncorrectSymbolError as symbol:
            debug.error('Incorrect symbol: ' + str(symbol), exitcodes.EXIT_INCORRECT_SYMBOL)
        except translator.NestedPredicateError as formula:
            debug.error('You nested a predicate in formula: ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except translator.NotEnoughArguments as formula:
            debug.error('You have not given valid amount of arguments in function/predicate: ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except translator.IncorrectFormulaError as formula:
            debug.error('Incorrect formula: ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except:
            debug.error(f'Unknown error. Report the developer ({DEVELOPER_URL})', exitcodes.EXIT_UNKNOWN_ERROR)

if __name__ == '__main__':
    main()

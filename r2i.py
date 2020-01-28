#!/usr/bin/env python3

import re
import sys
import string
import json

from app import lexer, parser, render, mts
from app.debug import error, panic

DEVELOPER_URL = 'https://github.com/qwercik/r2i'

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()
        
        try:
            tokensStream = lexer.tokenizeRpnFormula(rpnFormula)
            syntaxTree = parser.parse(tokensStream)
            infixFormula = render.renderInfix(syntaxTree)

            print('Formuła spełnialna' if mts.checkFormulaSatisfiable(syntaxTree) else 'Formuła niespełnialna')

        except lexer.UnrecognizableSymbolError as symbol:
            error(f'Unrecognizable symbol {symbol}')
        except parser.NestedPredicateError as e:
            nestedPredicateName, currentTokenType, currentTokenName = e.args[0]
            error(f'Predicate {nestedPredicateName} nested in {currentTokenType} {currentTokenName}')
        except parser.ArgumentOfOperatorShouldBeALogicalFormulaError as operator:
            error(f'Argument of {operator} operator must be a logical formula')
        except parser.FirstArgumentOfQuantifierShouldBeAVariableError as quantifierType:
            error(f'First argument of {quantifierType} must be a variable')
        except parser.SecondArgumentOfQuantifierShouldBeALogicalFormulaError as quantifierType:
            error(f'Second argument of {quantifierType} must be a logical formula')
        except parser.IncorrectArgumentsNumberError as tokenType:
            error(f'Incorrect arguments number in {tokenType}')
        except parser.EmptyFormula:
            error(f'Empty formula')
        #except:
        #    panic(255, f'Unknown error ocurred. Report the developer: {DEVELOPER_URL}')

if __name__ == '__main__':
    main()

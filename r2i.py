#!/usr/bin/env python3

import re
import sys
import string
import json

from app import lexer, parser, render, mts
from app.debug import error, panic

DEVELOPER_URL = 'https://github.com/qwercik/r2i'

def main():
    line1 = input().strip()
    syntaxTree1 = parser.parse(lexer.tokenizeRpnFormula(line1))

    line2 = input().strip()
    syntaxTree2 = parser.parse(lexer.tokenizeRpnFormula(line2))

    print(render.renderInfix(syntaxTree1))
    print(render.renderInfix(syntaxTree2))

    print(mts.compareFormulas(syntaxTree1, syntaxTree2))

    for line in sys.stdin:
        rpnFormula = line.strip()
        
        try:
            tokensStream = lexer.tokenizeRpnFormula(rpnFormula)
            syntaxTree = parser.parse(tokensStream)

            import pprint
            pprint.pprint(syntaxTree)
            syntaxTree = mts.removeRedundantNegations(syntaxTree) #TODO: remove
            
            print(f'Found constants: ', mts.findAllConstants(syntaxTree))
            infixFormula = render.renderInfix(syntaxTree)

            print(infixFormula)
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
        except Exception as e:
            print(e)
            panic(255, f'Unknown error ocurred. Report the developer: {DEVELOPER_URL}')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import re
import sys
import string
import lexer
import debug
import utilities

EXIT_INCORRECT_SYMBOL = 1
EXIT_INCORRECT_FORMULA = 2
EXIT_UNKNOWN_ERROR = 255

class IncorrectFormulaError(Exception):
    pass

def translateRpnToInfix(rpnFormula):
    stack = []
    infixFormula = ''

    tokens = lexer.tokenizeRpn(rpnFormula)
    for token in tokens:
        if token['category'] == 'value':
            stack.append(token)
        elif token['category'] == 'expression_with_parenthesis':
            symbol, arity = token['data']
            stack, arguments = utilities.popSeveral(stack, int(arity))
            
            textOutput = symbol + '(' + ', '.join(map(lambda arg: arg['data'], arguments)) + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
            
            if int(arity) == 0:
                debug.warning('Predykat powinien mieć przynajmniej jeden argument')

        elif token['category'] == 'unary_operator':
            symbol = token['data']
            argument = stack.pop()

            textOutput = '(' + symbol + ' ' + argument['data'] + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'binary_operator':
            symbol = token['data']
            stack, arguments = utilities.popSeveral(stack, 2)

            textOutput = '(' + arguments[0]['data'] + ' ' + symbol + ' ' + arguments[1]['data'] + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'quantifier':
            symbol = token['data']
            stack, arguments = utilities.popSeveral(stack, 2)

            textOutput = '(' + symbol + ' ' + arguments[0]['data'] + ' ' + arguments[1]['data'] + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
    
    if len(stack) != 1:
        raise IncorrectFormulaError(rpnFormula)

    infixFormula = stack[0]['data']
    return infixFormula

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()

        try:
            infixFormula = translateRpnToInfix(rpnFormula)
            print(infixFormula)
        except lexer.IncorrectSymbolError as symbol:
            debug.error('Incorrect symbol ' + str(symbol), EXIT_INCORRECT_SYMBOL)
        except IncorrectFormulaError as formula:
            debug.error('Incorrect formula ' + str(formula), EXIT_INCORRECT_FORMULA)
        except:
            debug.error('Unknown error. Report the developer', EXIT_UNKNOWN_ERROR)

if __name__ == '__main__':
    main()

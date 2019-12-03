#!/usr/bin/env python3

import re
import sys
import string
import lexer
import debug
import utilities
import exitcodes

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
            arity = int(arity)

            arguments = utilities.popSeveral(stack, arity)
            
            argumentsList = ', '.join(map(lambda arg: arg['data'], arguments))
            textOutput = f'{symbol}({argumentsList})'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
            
            if arity == 0:
                debug.warning('Predykat powinien mieć przynajmniej jeden argument')

        elif token['category'] == 'unary_operator':
            symbol = token['data']
            argument = stack.pop()

            argumentSymbol = argument['data']
            textOutput = f'({symbol} {argumentSymbol})'

            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'binary_operator':
            symbol = token['data']
            arguments = utilities.popSeveral(stack, 2)
            
            leftOperandSymbol = arguments[0]['data']
            rightOperandSymbol = arguments[1]['data']

            textOutput = f'({leftOperandSymbol} {symbol} {rightOperandSymbol})'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'quantifier':
            symbol = token['data']
            arguments = utilities.popSeveral(stack, 2)

            variableSymbol = arguments[0]['data']
            formula = arguments[1]['data']

            textOutput = f'({symbol} {variableSymbol} {formula})'
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
            debug.error('Incorrect symbol ' + str(symbol), exitcodes.EXIT_INCORRECT_SYMBOL)
        except IncorrectFormulaError as formula:
            debug.error('Incorrect formula ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except:
            debug.error('Unknown error. Report the developer', exitcodes.EXIT_UNKNOWN_ERROR)

if __name__ == '__main__':
    main()

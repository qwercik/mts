#!/usr/bin/env python3

import re
import sys
import string
import lexer

def popFew(inputList, count):
    data = inputList[-count:]
    inputList = inputList[:-count]
    return (inputList, data)

def translateRpnToInfix(rpnFormula):
    stack = []
    infixFormula = ''

    tokens = lexer.tokenizeRpn(rpnFormula)
    for token in tokens:
        if token['category'] == 'value':
            stack.append(token)
        elif token['category'] == 'expression_with_parenthesis':
            symbol, arity = token['data']
            stack, arguments = popFew(stack, int(arity))
            
            textOutput = symbol + '(' + ', '.join(map(lambda arg: arg['data'], arguments)) + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'unary_operator':
            symbol = token['data']
            argument = stack.pop()

            textOutput = '(' + symbol + ' ' + argument['data'] + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'binary_operator':
            symbol = token['data']
            stack, arguments = popFew(stack, 2)

            textOutput = '(' + arguments[0]['data'] + ' ' + symbol + ' ' + arguments[1]['data'] + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
        elif token['category'] == 'quantifier':
            symbol = token['data']
            stack, arguments = popFew(stack, 2)

            textOutput = '(' + symbol + ' ' + arguments[0]['data'] + ' ' + arguments[1]['data'] + ')'
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
    
    infixFormula = stack[0]['data']
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

import lexer
import debug
import utilities

class IncorrectFormulaError(Exception):
    pass

class NestedPredicateError(Exception):
    pass

class NotEnoughArguments(Exception):
    pass

def predicateInText(text):
    for letter in 'pqrstuvwxyz':
        if letter in text:
            return True

    return False

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

            if arity == 0:
                debug.warning('Predicate should have at least one argument')

            if len(stack) < arity:
                raise NotEnoughArguments(rpnFormula)

            arguments = utilities.popSeveral(stack, arity)
            
            argumentsList = ', '.join(map(lambda arg: arg['data'], arguments))
            argumentsListInBrackets = f'({argumentsList})'

            if predicateInText(argumentsList):
                raise NestedPredicateError(rpnFormula)

            textOutput = f'{symbol}' + (argumentsListInBrackets if arity != 0 else '')
            stack.append({ 'type': 'text', 'category': 'text', 'data': textOutput })
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


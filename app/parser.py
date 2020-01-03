from app.utilities import popSeveral

tokensTypesCategories = {
    'constant': 'value',
    'variable': 'value',
    'function': 'expression_with_parenthesis',
    'predicate': 'expression_with_parenthesis',
    'negation': 'unary_operator',
    'conjunction': 'binary_operator',
    'disjunction': 'binary_operator',
    'implication': 'binary_operator',
    'equivalence': 'binary_operator',
    'exclusionary_alternative': 'binary_operator',
    'universal_quantifier': 'quantifier',
    'existential_quantifier': 'quantifier'
}

def tokenTypeCategory(token):
    return tokensTypesCategories[token['type']]


class IncorrectArgumentsNumberError(Exception):
    pass

class NestedPredicateError(Exception):
    pass

class ArgumentOfOperatorShouldBeALogicalFormulaError(Exception):
    pass

class SecondArgumentOfQuantifierShouldBeALogicalFormulaError(Exception):
    pass

class FirstArgumentOfQuantifierShouldBeAVariableError(Exception):
    pass


def isLogicalFormula(formula):
    return formula['type'] == 'predicate' or formula['category'] in ['unary_operator', 'binary_operator', 'quantifier']

def createNodeWithCurrentToken(token, stack):
    category = tokenTypeCategory(token)
    if category == 'value':
        return {
            'name': token['data']
        }
    elif category == 'expression_with_parenthesis':
        name, arity = token['data']
        arity = int(arity) # It do not throw exception due to lexer
        arguments = popSeveral(stack, arity)
        
        # Predicates must not be nested neither in functions nor in other predicates
        for argument in arguments:
            if argument['type'] == 'predicate':
                nestedPredicateName = argument['name']
                currentTokenType = token['type']
                raise NestedPredicateError((nestedPredicateName, currentTokenType, name))

        return {
            'name': name,
            'arguments': arguments
        }
    elif category == 'unary_operator' or category == 'binary_operator':
        operator = token['data']
        arity = 1 if category == 'unary_operator' else 2

        arguments = popSeveral(stack, arity)
        for argument in arguments:
            if not isLogicalFormula(argument):
                raise ArgumentOfOperatorShouldBeALogicalFormulaError(operator)

        return {
            'arguments': arguments
        }
    elif category == 'quantifier':
        formula = stack.pop()
        variable = stack.pop()
        
        if variable['type'] != 'variable':
            raise FirstArgumentOfQuantifierShouldBeAVariableError(token['type'])

        if not isLogicalFormula(formula):
            raise SecondArgumentOfQuantifierShouldBeALogicalFormulaError(token['type'])

        return {
            'variable': variable,
            'formula': formula
        }

def parse(tokensStream):
    stack = []
    for token in tokensStream:
        try:
            node = createNodeWithCurrentToken(token, stack)
        except IndexError:
            # Stack pop error
            tokenType = token['type']
            raise IncorrectArgumentsNumberError(tokenType)
        except:
            # Re-raise application errors thrown in createNodeWithCurrentToken()
            raise

        category = tokenTypeCategory(token)

        stack.append({
            'type': token['type'],
            'category': category,
            'symbol': token['symbol'],
            **node,
        })

    if len(stack) != 1:
        raise IncorrectArgumentsNumberError('formula')

    return stack.pop()



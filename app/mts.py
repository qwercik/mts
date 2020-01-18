import itertools

def removeRedundantNegations(syntaxTree):
    while syntaxTree['type'] == 'negation' and syntaxTree['arguments'][0]['type'] == 'negation':
        syntaxTree = syntaxTree['arguments'][0]['arguments'][0]

    return syntaxTree

def findAllConstants(syntaxTree):
    if syntaxTree['type'] == 'variable':
        return []
    elif syntaxTree['type'] == 'constant':
        return [syntaxTree['symbol']]
    elif syntaxTree['category'] in ['expression_with_parenthesis', 'unary_operator', 'binary_operator']:
        constants = []
        for argument in syntaxTree['arguments']:
            constants += findAllConstants(argument)
        return constants
    elif syntaxTree['category'] == 'quantifier':
        return findAllConstants(syntaxTree['formula'])
        
def doesNodeContainComplementaryLiterals(node):
    for formula1, formula2 in itertools.combinations(node, 2):
        # Rebember about not!
        if formula1['type'] != 'predicate' and formula2['type'] != 'predicate':
            continue

        if formula1['type'] == 'negation' and formula1['arguments'][0]['type'] == 'predicate':
            if formula1['arguments'][0]['symbol'] == formula2['symbol']:
                return True
        
        if formula2['type'] == 'negation' and formula2['arguments'][0]['type'] == 'predicate':
            if formula1['symbol'] == formula2['arguments'][0]['symbol']:
                return True

    return False
            

def isSatisfiable(syntaxTree, constants=[]):
    pass


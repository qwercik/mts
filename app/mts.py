def findAllConstants(syntaxTree):
    if syntaxTree['type'] == 'variable':
        return []
    elif syntaxTree['type'] == 'constant':
        return [syntaxTree['name']]
    elif syntaxTree['category'] in ['expression_with_parenthesis', 'unary_operator', 'binary_operator']:
        constants = []
        for argument in syntaxTree['arguments']:
            constants += findAllConstants(argument)
        return constants
    elif syntaxTree['category'] == 'quantifier':
        return findAllConstants(syntaxTree['formula'])

def compareFormulas(syntaxTree1, syntaxTree2):
    if syntaxTree1['type'] != syntaxTree2['type']:
        return False

    if syntaxTree1['category'] == 'value':
        return syntaxTree1['name'] == syntaxTree2['name']
    elif syntaxTree1['category'] in ['expression_with_parenthesis', 'unary_operator', 'binary_operator']:
        if len(syntaxTree1['arguments']) != len(syntaxTree2['arguments']):
            return False
        
        for index in range(len(syntaxTree1['arguments'])):
            if not compareFormulas(syntaxTree1['arguments'][index], syntaxTree2['arguments'][index]):
                return False

        return True
    elif syntaxTree1['category'] == 'quantifier':
        return syntaxTree1['variable'] == syntaxTree2['variable'] and compareFormulas(syntaxTree1['formula'], syntaxTree2['formula'])

def isLiteral(formula):
    return formula['type'] == 'predicate' or (formula['type'] == 'negation' and formula['arguments'][0]['type'] == 'predicate')

def extractAtomFromLiteral(formula):
    if formula['type'] == 'predicate':
        return formula 
    return formula['arguments'][0]

def areLiteralsComplementary(literal1, literal2):
    return compareFormulas(
        extractAtomFromLiteral(literal1),
        extractAtomFromLiteral(literal2)
    )

def lookThroughNode(node):
    literals = []
    for index, formula in enumerate(node):
        node[index] = removeRedundantNegations(formula)

        if isLiteral(formula):
            for literal in literals:
                if areLiteralsComplementary(formula, literal):
                    print('Znalazłem literały komplementarne!')
                    break
            else:
                literals.push(formula)

def existComplementaryLiteral(literal, listOfLiterals):
    for currentLiteral in listOfLiterals:
        if areLiteralsComplementary(currentLiteral, literal):
            return True

    return False
            
def isSatisfiable(syntaxTree, constants=[]):
    syntaxTree = removeRedundantNegations(syntaxTree)
    if not constants:
        constants = findAllConstants(syntaxTree)
    
    node = [syntaxTree]
    literals = []
    formulasTypes = {
        'alfa': [],
        'beta': [],
        'gamma': [],
        'delta': [],
    }

    while True:
        for formula in node:
            if isLiteral(formula):
                if existComplementaryLiteral(formula, literals):
                    return False
                
                literals.append(formula)
            else:
                # Detect formula type
                pass




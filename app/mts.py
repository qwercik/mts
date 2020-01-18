alfaBetaRules = {
    # Double negation is also alfa
    'conjunction': 'alfa',
    'equivalence': 'alfa',
    'disjunction': 'beta',
    'implication': 'beta',
    'exclusionary_alternative': 'beta'
}

gammaDeltaRules = {
    'universal_quantifier': 'gamma',
    'existential_quantifier': 'delta'
}

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

def existComplementaryLiteral(literal, listOfLiterals):
    for currentLiteral in listOfLiterals:
        if areLiteralsComplementary(currentLiteral, literal):
            return True

    return False

def detectRuleType(syntaxTree):
    if syntaxTree['type'] == 'negation':
        if syntaxTree['arguments'][0]['type'] == 'negation':
            return 'alfa'
        elif syntaxTree['arguments'][0]['type'] in alfaBetaRules:
            return 'beta' if alfaBetaRules[syntaxTree['arguments'][0]['type']] == 'alfa' else 'alfa'
        else:
            return 'delta' if gammaDeltaRules[syntaxTree['arguments'][0]['type']] == 'gamma' else 'gamma'
    else:
        if syntaxTree['type'] in alfaBetaRules:
            return alfaBetaRules[syntaxTree['type']]
        else:
            return gammaDeltaRules[syntaxTree['type']]


def isSatisfiable(syntaxTree, constants=[]):
    if not constants:
        constants = findAllConstants(syntaxTree)
    
    node = [syntaxTree]
    while True:
        literals = []
        formulasTypes = {
            'alfa': [],
            'beta': [],
            'gamma': [],
            'delta': [],
        }
        
        for formula in node:
            if isLiteral(formula):
                if existComplementaryLiteral(formula, literals):
                    return False
                
                literals.append(formula)
            else:
                ruleType = detectRuleType(formula) 
                formulasTypes[ruleType].append(formula)

        # Priority of running rules:
        if formulasTypes['alfa']:
            pass
        elif formulasTypes['delta']:
            pass
        elif formulasTypes['beta']:
            pass
        elif formulasTypes['gamma']:
            pass

        return False



from app.debug import *
from app import render

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

constantsNames = ['a', 'b', 'c', 'd', 'e']

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
    # One is negation and another no
    return literal1['type'] != literal2['type'] and compareFormulas(
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

def negateFormula(syntaxTree):
    return {
        'type': 'negation',
        'category': 'unary_operator',
        'symbol': '~',
        'arguments': [syntaxTree]
    }

def createImplication(antecedentTree, consequentTree):
    return {
        'type': 'implication',
        'category': 'binary_operator',
        'symbol': 'IMPLIES',
        'arguments': [antecedentTree, consequentTree]
    }

def runAlfaRule(syntaxTree):
    if syntaxTree['type'] == 'negation':
        child = syntaxTree['arguments'][0]
        arguments = syntaxTree['arguments'][0]['arguments']

        if child['type'] == 'disjunction':
            return [
                negateFormula(arguments[0]),
                negateFormula(arguments[1])
            ]
        elif child['type'] == 'implication':
            return [
                arguments[0],
                negateFormula(arguments[1])
            ]
        elif child['type'] == 'negation':
            return [
                arguments[0]
            ]
        elif child['type'] == 'exclusionary_alternative':
            return [
                createImplication(arguments[0], arguments[1]),
                createImplication(arguments[1], arguments[0])
            ]
    else:
        arguments = syntaxTree['arguments']

        if syntaxTree['type'] == 'conjunction':
            return [
                arguments[0],
                arguments[1]
            ]
        elif syntaxTree['type'] == 'equivalence':
            return [
                createImplication(arguments[0], arguments[1]),
                createImplication(arguments[1], arguments[0])
            ]

def substituteVariable(syntaxTree, variable, constant):
    print('O, widzę że próbujesz coś tu podstawić :D W sensie', variable, 'na', constant)
    print(syntaxTree['type'])
    if syntaxTree['type'] == 'variable' and syntaxTree['name'] == variable:
        print('Zamieniam', syntaxTree['name'], 'na', constant)
        syntaxTree['type'] = 'constant'
        syntaxTree['name'] = constant
        syntaxTree['symbol'] = constant
    elif syntaxTree['category'] in ['expression_with_parenthesis', 'unary_operator', 'binary_operator']:
        for argument in syntaxTree['arguments']:
            substituteVariable(argument, variable, constant)
    elif syntaxTree['category'] == 'quantifier' and syntaxTree['variable']['name'] != variable:
        substituteVariable(syntaxTree['formula'], variable, constant)

def isSatisfiable(syntaxTree, usedConstants=[]):
    if not usedConstants:
        usedConstants = findAllConstants(syntaxTree) or constantsNames[:1]
        usedConstants.sort()
    
    warning('Wszystkie stałe: ', usedConstants)

    node = [syntaxTree]
    while True:
        literals = []
        formulasTypes = {
            'alfa': [],
            'beta': [],
            'gamma': [],
            'delta': [],
        }
        
        for index, formula in enumerate(node):
            if isLiteral(formula):
                if existComplementaryLiteral(formula, literals):
                    return False
                
                literals.append(formula)
            else:
                ruleType = detectRuleType(formula) 
                formulasTypes[ruleType].append(index)
        
        # Priority of running rules:
        if formulasTypes['alfa']:
            print('Wywołuję formułę alfa')
            formula = node.pop(formulasTypes['alfa'].pop())
            node += runAlfaRule(formula)
        elif formulasTypes['delta']:
            print('Wywołuję formułę delta.')
            
            newConstant = None
            for name in constantsNames:
                if not name in usedConstants:
                    newConstant = name
                    break
            else:
                error('Nie mogę znaleźć nowej nazwy zmiennej!')
            
            v = formula['variable']['name']
            print(f'Podstawię stałą {newConstant} pod zmienną {v}')
            
            formula = node.pop(formulasTypes['delta'].pop())
            print('Formuła przed podstawieniem:', render.renderInfix(formula))
            substituteVariable(formula['formula'], formula['variable']['name'], newConstant)
            print('Formuła po podstawieniu:', render.renderInfix(formula['formula']))

            node.append(formula['formula'])
        elif formulasTypes['beta']:
            pass
        elif formulasTypes['gamma']:
            pass
        else:
            return True
        


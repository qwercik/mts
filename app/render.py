operatorsPriority = {
    'negation': 4,
    'exclusionary_alternative': 3,
    'conjunction': 2,
    'disjunction': 1,
    'equivalence': 0,
    'implication': 0
}

associativeOperators = ['conjunction', 'disjunction', 'exclusionary_alternative']

def operatorPriority(operator):
    return operatorsPriority[operator]

def renderInfix(syntaxTree):
    category = syntaxTree['category']
    if category == 'value':
        return syntaxTree['name']
    elif category == 'expression_with_parenthesis':
        name = syntaxTree['name']
        
        arguments = []
        for argument in syntaxTree['arguments']:
            arguments.append(renderInfix(argument))
        argumentsList = ', '.join(arguments)
        
        return f'{name}({argumentsList})'
    elif category == 'unary_operator':
        operator = syntaxTree['symbol']
        argument = syntaxTree['arguments'][0]
        argumentString = renderInfix(argument)
        
        if argument['category'] in ['unary_operator', 'binary_operator']:
            argumentString = f'({argumentString})'
        
        return f'{operator}{argumentString}'
    elif category == 'binary_operator':
        operator = syntaxTree['symbol']
        argumentsStrings = list(map(lambda x: renderInfix(x), syntaxTree['arguments']))

        for index, argumentString in enumerate(argumentsStrings):
            argument = syntaxTree['arguments'][index]
            
            if argument['category'] == 'binary_operator' and (argument['type'] != syntaxTree['type'] or not argument['type'] in associativeOperators):
                argumentsStrings[index] = f'({argumentString})'
        
        return f'{argumentsStrings[0]} {operator} {argumentsStrings[1]}'
    elif category == 'quantifier':
        quantifier = syntaxTree['symbol']
        variable = renderInfix(syntaxTree['variable'])
        formula = renderInfix(syntaxTree['formula'])

        if syntaxTree['formula']['category'] == 'binary_operator':
            formula = f'({formula})'

        return f'{quantifier}{variable} {formula}'

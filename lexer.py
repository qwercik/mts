import re

class IncorrectTokenError(Exception):
    pass

tokensTypes = {
    'constant': r'^[a-e]$',
    'variable': r'^[A-Z]$',
    'function': r'^([f-n])/(\d)$',
    'predicate': r'^([p-z])/(\d)$',
    'negation': r'^(?:NOT|~|¬)$',
    'conjunction': r'^(?:AND|&|∧)$',
    'disjunction': r'^(?:OR|\||∨)$',
    'implication': r'^(?:IMPLIES|→)$',
    'equivalence': r'^(?:IFF|↔)$',
    'exclusionary_alternative': r'^(?:XOR|⊕)$',
    'universal_quantifier': r'^(?:FORALL|∀)$',
    'existential_quantifier': r'^(?:EXISTS|∃)$'
}

tokensCategories = {
    'value': ['constant', 'variable'],
    'expression_with_parenthesis': ['function', 'predicate'],
    'unary_operator': ['negation'],
    'binary_operator': ['conjunction', 'disjunction', 'implication', 'equivalence', 'exclusionary_alternative'],
    'quantifier': ['universal_quantifier', 'existential_quantifier']
}

def tokenizeRpn(rpnFormula):
    tokens = []

    symbols = rpnFormula.split()
    for symbol in symbols:
        for tokenType, regex in tokensTypes.items():
            matchResult = re.findall(regex, symbol)
            if matchResult:
                tokens.append({
                    'type': tokenType,
                    'category': tokenCategory(tokenType),
                    'data': matchResult[0]
                })
                break
        else:
            raise IncorrectTokenError(token)

    return tokens

def tokenCategory(tokenType):
    for tokenCategory, types in tokensCategories.items():
        if tokenType in types:
            return tokenCategory

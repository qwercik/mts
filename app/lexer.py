import re

class UnrecognizableSymbolError(Exception):
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

def tokenizeRpnFormula(rpnFormula):
    tokens = []

    symbols = rpnFormula.split()
    for symbol in symbols:
        for tokenType, regex in tokensTypes.items():
            matchResult = re.findall(regex, symbol)
            if matchResult:
                tokens.append({
                    'type': tokenType,
                    'symbol': symbol,
                    'data': matchResult[0]
                })
                break
        else:
                raise UnrecognizableSymbolError(symbol)

    return tokens


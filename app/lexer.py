import re

class UnrecognizableSymbolError(Exception):
    pass

tokensTypes = {
    'constant': r'^[a-e]$',
    'variable': r'^[t-z]$',
    'function': r'^([f-n])/(\d+)$',
    'predicate': r'^([p-z])/(\d+)$',
    'negation': r'^~$',
    'conjunction': r'^&$',
    'disjunction': r'^\|$',
    'implication': r'^->$',
    'equivalence': r'^<->$',
    'exclusionary_alternative': r'^\+$',
    'universal_quantifier': r'^A$',
    'existential_quantifier': r'^E$'
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


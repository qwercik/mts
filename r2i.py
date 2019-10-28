#!/usr/bin/env python3

import sys
import string

class IncorrectTokenError(Exception):
    pass

tokensDescription = {
    'constant': ['a', 'b', 'c', 'd', 'e'],
    'variable': list(string.ascii_uppercase),
    'function': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
    'predicate': ['p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z'],
    'negation': ['NOT', '~', '¬'],
    'conjunction': ['AND', '&', '∧'],
    'disjunction': ['OR', '|', '∨'],
    'implication': ['IMPLIES', '→'],
    'equivalence': ['IFF', '↔'],
    'exclusionary_alternative': ['XOR', '⊕'],
    'universal_quantifier': ['FORALL', '∀'],
    'existential_quantifier': ['EXISTS', '∃']
}

def parseRpn(rpnFormula):
    tokens = rpnFormula.split()
    for token in tokens:
        splitted = token.split('/')

        if len(splitted) == 2:
            symbol, arity = splitted
            if symbol in tokensDescription['function']:
                print('function')
            elif symbol in tokensDescription['predicate']:
                print('predicate')
            else:
                raise IncorrectTokenError(token)
        else:
            tokenType = None
            for key, tokenTypeLetters in tokensDescription.items():
                if token in tokenTypeLetters:
                    tokenType = key
            
            if tokenType == None:
                raise IncorrectTokenError(token)

            print(tokenType)

    return ''

def translateRpnToInfix(rpnFormula):
    parsed = parseRpn(rpnFormula)
    return ''

def main():
    for line in sys.stdin:
        rpnFormula = line.strip()
        print(translateRpnToInfix(rpnFormula))

if __name__ == '__main__':
    main()

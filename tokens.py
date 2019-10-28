tokensDescription = {
    'constant': {
        'regex': r'^[a-e]$'
    },
    'variable': {
        'regex': r'^[A-Z]$'
    },
    'function': {
        'regex': r'^[f-n]/\d$'
    },
    'predicate': {
        'regex': r'^[p-z]/\d$'
    },
    'negation': {
        'regex': r'^(?:NOT|~|¬)$',
        'output': '~'
    },
    'conjunction': {
        'regex': r'^(?:AND|&|∧)$',
        'output': '&'
    },
    'disjunction': {
        'regex': r'^(?:OR|\||∨)$',
        'output': '|'
    },
    'implication': {
        'regex': r'^(?:IMPLIES|→)$',
        'output': '→'
    },
    'equivalence': {
        'regex': r'^(?:IFF|↔)$',
        'output': '↔'
    },
    'exclusionary_alternative': {
        'regex': r'^(?:XOR|⊕)$',
        'output': '⊕'
    },
    'universal_quantifier': {
        'regex': r'^(?:FORALL|∀)$',
        'output': '∀'
    },
    'existential_quantifier': {
        'regex': r'^(?:EXISTS|∃)$',
        'output': '∃'
    }
}

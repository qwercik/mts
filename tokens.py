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

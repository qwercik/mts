# mts

Check satisfiablity of first-order logic formulas

## Installation

```bash
git clone https://github.com/qwercik/mts
cd mts
chmod +x mts.py
```

## Usage

```bash
./mts.py
```

Type formulas (in Reverse Polish Notation) to the standard input.
Each formula should end with a single newline character. You will get answer in the following lines.

# Example

```
>>> X X p/1 Y Y p/1 ~ FORALL a p/1 ~ & | EXISTS ~
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a)))}, {a})
Run gamma rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ (p(a) | (FORALL Y ~ p(Y) & ~ p(a)))}, {a})
Run alpha rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ (FORALL Y ~ p(Y) & ~ p(a))}, {a})
Run beta rule

Branch 0
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ FORALL Y ~ p(Y)}, {a})
Run delta rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ (~ p(b))}, {a, b})
Run alpha rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(b)}, {a, b})
Run gamma rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(b), ~ (p(b) | (FORALL Y ~ p(Y) & ~ p(a)))}, {a, b})
Run alpha rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(b), ~ p(b), ~ (FORALL Y ~ p(Y) & ~ p(a))}, {a, b})
Branch 0 unsatisfiable


Branch 1
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ (~ p(a))}, {a})
Run alpha rule
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(a)}, {a})
Branch 1 unsatisfiable

Unsatisfiable
```

## Syntax

### Terms

| Syntax element | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| Constant       | Constant is a single, small letter from the following set: a, b, c, d, e |
| Variable       | Variable is a single, small letter from the following set: t, u, w, v, x, y, z |
| Function       | Function is defined by its' name and arity (arguments number). The name must be from the following set: f, h, h, i, j, k, l, m, n. The arity is a number given after slash.<br />Example: f/3 means function f, that takes three arguments<br />It can take only terms as arguments (constants, variables or other functions) |

**Predicates**

| Syntax element | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| Predicate      | Predicate is defined by its' name and arity (arguments number). The name must be from the following set: p, q, r, s, t, u, v, w, x, y, z. The arity is a number given after slash.<br />Example: q/2 means a predicate q, that takes two arguments.<br />Predicate can take only terms as arguments (constants, variables or other functions) |

### Operators

It's required that each operand has a logical value (so it must be a single predicate or complex formula created with predicates, operators and quantifiers).

#### Unary operator

| Syntax element | Description                          |
| -------------- | ------------------------------------ |
| Negation       | Negation is represented by symbol: ~ |

#### Binary operators

| Syntax element        | Description                               |
| --------------------- | ----------------------------------------- |
| Conjunction           | Conjunction is represented by symbol: &   |
| Disjunction           | Disjunction is represented by symbol: \|  |
| Implication           | Implication is represented by symbol: ->  |
| Equivalence           | Equivalence is represented by symbol: <-> |
| Exclusive disjunction | Exclusive disjunction is represented: +   |

### Quantifiers

| Syntax element         | Description                                        |
| ---------------------- | -------------------------------------------------- |
| Universal quantifier   | Universal quantifier is represented by symbol: A   |
| Existential quantifier | Existential quantifier is represented by symbol: E |


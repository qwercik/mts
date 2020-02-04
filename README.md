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

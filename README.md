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
Uruchamiam regułę gamma
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ (p(a) | (FORALL Y ~ p(Y) & ~ p(a)))}, {a})
Uruchamiam formułę alfa
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ (FORALL Y ~ p(Y) & ~ p(a))}, {a})
Uruchamiam regułę beta

Gałąź 0
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ FORALL Y ~ p(Y)}, {a})
Uruchamiam regułę delta
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ (~ p(b))}, {a, b})
Uruchamiam formułę alfa
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(b)}, {a, b})
Uruchamiam regułę gamma
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(b), ~ (p(b) | (FORALL Y ~ p(Y) & ~ p(a)))}, {a, b})
Uruchamiam formułę alfa
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(b), ~ p(b), ~ (FORALL Y ~ p(Y) & ~ p(a))}, {a, b})
Gałąź 0 niespełnialna


Gałąź 1
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), ~ (~ p(a))}, {a})
Uruchamiam formułę alfa
({~ EXISTS X (p(X) | (FORALL Y ~ p(Y) & ~ p(a))), ~ p(a), p(a)}, {a})
Gałąź 1 niespełnialna

Formuła niespełnialna
```

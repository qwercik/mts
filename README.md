# r2i
Script that converts first-logic-logic formulas from Reverse Polish Notation to infix notation.

## Installation
```bash
git clone https://github.com/qwercik/r2i
cd r2i
chmod +x r2i.py
```

## Usage
```bash
./r2i.py
```
Type RPN formulas to the standard input. Each formula should end with a single newline character. You will get converted formula on the standard output.

## Example
Input:
```
X X p/1 X q/1 → FORALL ~ X X p/1 FORALL X X q/1 FORALL → →
X Y X Y X Y p/6 Y X Y X Y X Y X q/7 EXISTS IFF NOT
```

Output:
```
((~ (FORALL X (p(X) → q(X)))) → ((FORALL X p(X)) → (FORALL X q(X))))
(NOT (p(X, Y, X, Y, X, Y) IFF (EXISTS Y q(X, Y, X, Y, X, Y, X))))
```

## Testing
If you would like to test an app with some predefined tests, run script test.py
```
chmod +x test.py
./test.py
```

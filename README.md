# Report 2 - Equivalence Relation Checker

## Requirements
- Python 3.8 or later
- No external libraries required

## Run
Open a terminal in this folder and run:

```bash
python report2_equivalence_checker.py
```

## Features
1. Accepts a 5 x 5 binary relation matrix.
2. Checks reflexive, symmetric, and transitive properties separately.
3. Displays equivalence classes when the relation is an equivalence relation.
4. Implements reflexive, symmetric, and transitive closures.
5. Uses Warshall's algorithm for transitive closure and can display its intermediate matrices.
6. Includes a built-in example matrix.

## Input format
Enter five values (0 or 1) for each row, separated by spaces.
For example: `1 0 0 1 0`

The built-in example has equivalence classes `{1, 2}` and `{3, 4, 5}`.


from sympy import symbols
from sympy.logic.boolalg import (
    Implies, Equivalent, to_cnf
)

# Define propositions
P, Q, R = symbols('P Q R')

# Input FOL-style logical expression
expr = Implies(P, Q) | R

print("Original Expression:")
print(expr)

# Convert into CNF
cnf_expr = to_cnf(expr, simplify=True)

print("\nConjunctive Normal Form (CNF):")
print(cnf_expr)

import numpy as np
import integrate_simpson
from sympy import symbols, Eq, solve, simplify, lambdify

# f(x) = x ** 2 + 2 <=> f^-1(y) = sqrt(y - 2)

f = lambda y: np.sqrt(y - 2)

# # Traženje inverzne funkcije pomoću sympy biblioteke
# x, y = symbols("x y")
# n = Eq(y, x**2 + 2)
# s = solve(n, x)
# print(s)
# s = simplify(s[1])
# f = lambdify(y, s)


y1 = 2
y2 = 4

P = integrate_simpson.integrate_simpson(f, y1, y2, 100, 0.0)

print('P = ', P)

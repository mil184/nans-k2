import numpy as np
import integrate_simpson

f = lambda x: np.exp(x) + 2
g = lambda x: np.sqrt(x)

a = 2
b = 3

fg_sqr = lambda x: np.abs(f(x) ** 2 - g(x) ** 2)

V = np.pi * integrate_simpson.integrate_simpson(fg_sqr, a, b, 100, 0.0)

print('V = ', V)

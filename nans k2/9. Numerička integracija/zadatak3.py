import numpy as np
import integrate_simpson

f = lambda x: x ** 2
g = lambda x: np.sqrt(x)

a = 0
b = 2

fg = lambda x: np.abs(f(x) - g(x))

P = integrate_simpson.integrate_simpson(fg, a, b, 100, 0.0)

print('P = ', P)

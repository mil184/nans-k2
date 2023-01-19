import numpy as np
import integrate_simpson

f = lambda x: np.exp(2*x) / x

a = 1
b = 2

f_sqr = lambda x: f(x) ** 2

V = np.pi * integrate_simpson.integrate_simpson(f_sqr, a, b, 100, 0.0)

print('V = ', V)

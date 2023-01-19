import numpy as np
import integrate_simpson


# f(x) = x ** 2 + 2 <=> f^-1(y) = sqrt(y - 2)
f = lambda y: np.sqrt(y - 2)

a = 0
b = 4
y1 = a**2 + 2
y2 = b**2 + 2

# plava zapremina
f_sqr = lambda x: f(x) ** 2
V1 = np.pi * integrate_simpson.integrate_simpson(f_sqr, y1, y2, 100, 0.0)

# V2 = r2^2*pi*H2 (zapremina cilindra)
V2 = (b - a) ** 2 * np.pi * (y2 - 0)

# trazena zapremina
V = V2 - V1

print('V = ', V)

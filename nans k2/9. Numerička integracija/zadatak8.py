import numpy as np
import integrate_simpson

v = lambda t: t**2 - 2*t + 3

t0 = 0
t1 = 5

s = integrate_simpson.integrate_simpson(v, t0, t1, 100, 0.0)

print('s = ', s)

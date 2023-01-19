import numpy as np
import integrate_simpson

f = lambda x: np.exp(-(x**2)/2)

a = 0
b = 0.2

I = 2/np.sqrt(2*np.pi) * integrate_simpson.integrate_simpson(f, a, b, 100, 0.0)

print('I = ', I)

import numpy as np
import integrate_simpson

f = np.sin

a = 0
b = 3*np.pi/2

I = integrate_simpson.integrate_simpson(f, a, b, 100, 0.0)

print('I = ', I)

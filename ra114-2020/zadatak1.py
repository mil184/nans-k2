import numpy as np
from nans_lib_2 import integrate_simpson
import matplotlib.pyplot as plt

f = lambda x: np.sin(x/2) + 1
g= lambda x: np.cos(x/2) + 1

#a povrsina izmedju krivih
a = 0
b = np.pi*4

fg = lambda x: np.abs(f(x) - g(x))

P = integrate_simpson(fg, a, b, 100)
print('P = ',P)

#b zapremina dobijena rotacijom oko x ose

c=3*np.pi/2
d=3*np.pi

#povrsina obrtanja f oko x
#f_kvadrat = lambda x: f(x)**2
#Vf=np.pi*integrate_simpson(f_kvadrat, c, d,100)

#povrsina obrtanja g oko x
#g_kvadrat = lambda x: g(x)**2
#Vg=np.pi*integrate_simpson(g_kvadrat, c, d,100)

fgV = lambda x: np.abs(f(x)**2 - g(x)**2)

V=np.pi*integrate_simpson(fgV, c, d, 100)
print('V = ',V)





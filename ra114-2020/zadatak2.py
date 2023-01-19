import numpy as np
import matplotlib.pyplot as plt
from nans_lib_2 import f, df, ddf, finiteDifference, least_squares_regression, zeroFalsePosition

left = lambda *argv : ddf(argv[1]) - df(argv[1])
right = lambda *argv : (argv[0]-1)/2


#a

x1 = -1
fX1 = 1
x2 = 1
fX2 = -1
h = (x2 - x1) / 100

x = np.arange(x1, x2 + h, h)
fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)
plt.plot(x, fX)
plt.show()


#b

x1=1
fX1=1
x2=-1
fX2=-1
h=(x2-x1)/100

x=np.arange(x1, x2+h, h)
fX=finiteDifference(left, right, x1, fX1, x2, fX2, h)
plt.plot(x, fX, 'magenta')
#plt.show()

p = least_squares_regression(x, fX, 7)
x = np.linspace(x1, x2, 100)
pX = np.polyval(p, x)
plt.plot(x, pX, 'blue', [x1, x2], [0, 0], 'black')

pf = lambda x: np.polyval(p, x) - 0
x1, _ = zeroFalsePosition(pf, 0, 1)
print("Presek sa x-osom: ",x1)
plt.scatter(x1, np.polyval(p, x1), c='red')

plt.show()


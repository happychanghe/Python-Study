import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math as m

def nthpolynomial(n: int, k: float, x: np.ndarray, a: float):
    _yn = np.zeros(len(x))
    print(type(_yn))
    for i in range(0, n+1):
        _yn = _yn + k*np.power(np.e, a)*np.power(x-a, i)/m.factorial(i)         # why error when using += ??


    return _yn
    

a = 6.5                   # taylor series from x = a
_n = 5                 # x domain
x = np.arange(-_n*np.e+a, _n*np.e+a, 0.1)
k = 1                   # y scale
y1 = k*np.power(np.e, x)        # sin 
# yn = []
# towhatn = 20
# for n in range(0, towhatn):
#     _yn = nthpolynomial(n, k, x)
#     yn.append(_yn)

fig, axes = plt.subplots(1, 1)
# axes.set_ylim(-2*k, 2*k)
# axes.set_xlim(-_n + a, _n + a)
l1 = axes.plot(x, y1, label='e^x')
# l2; l3; l4; l5
# for n in range(towhatn):
#     axes.plot(x, yn[n], label=f'order of {n}')
for i in range(20):
    c = 1-i/20
    axes.plot(x, nthpolynomial(i, k, x, a), label=f'order of {i}', color=(c, c, c))
# axes.legend()
plt.show()

# TODO: animation 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math as m

def nthpolynomial(n: int, x: np.ndarray, a: float):
    _yn = np.zeros(len(x))
    # print(type(_yn))
    for i in range(0, n+1):
        # print(type(_yn))
        # print(type(np.cos(a)*np.power(x-a, i)/m.factorial(i)))
        _i=i%4
        if _i==1:
            _yn = _yn + np.cos(a)*np.power(x-a, i)/m.factorial(i)         # why error when using += ??
        elif _i==2:
            _yn += -np.sin(a)*np.power(x-a, i)/m.factorial(i)
        elif _i==3:
            _yn += -np.cos(a)*np.power(x-a, i)/m.factorial(i)
        elif _i==0:
            _yn += np.sin(a)*np.power(x-a, i)/m.factorial(i)
        else: 
            print("err!!!!!!!!!!!!!")
            exit()

    return _yn
    

a = 0                   # taylor series from x = a
_n = 5                 # x domain
x = np.arange(-_n*np.pi+a, _n*np.pi+a, 0.1)
# k = 1                   # y scale
y1 = np.sin(x)        # sin 
# yn = []
# towhatn = 20
# for n in range(0, towhatn):
#     _yn = nthpolynomial(n, k, x)
#     yn.append(_yn)

fig, axes = plt.subplots(1, 1)
axes.set_ylim(-2, 2)
axes.set_xlim(-_n*np.pi + a, _n*np.pi + a)
l1 = axes.plot(x, y1, label='sin')
# l2; l3; l4; l5
# for n in range(towhatn):
#     axes.plot(x, yn[n], label=f'order of {n}')

for i in range(7):
    c = 1-i/7
    axes.plot(x, nthpolynomial(i, x, a), label=f'order of {i}', color=(c, c, c))

# nnn = 10
# axes.plot(x, nthpolynomial(nnn, x, a), label=f'order of {nnn}', color=(0, 0, 0))
axes.legend()
plt.show()

# TODO: animation 
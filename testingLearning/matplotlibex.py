import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x=np.arange(-1*np.e, np.e, 0.1)
_cosh= np.cosh(x)
_sinh=np.sinh(x)
l1, = ax.plot(x, _cosh, label='cosh')
l2, = ax.plot(x, _sinh, label='sinh')
ax.legend(handles=[l1, l2], )

plt.show()
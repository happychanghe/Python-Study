#learning from: https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#ax.set_xlabel("time")
#ax.set_title("big title")
#ax.yaxis.set_minor_locator(0.5)
#ax.yaxis.set_major_locator(1)

# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
#rng = np.random.default_rng()
#rng.integers
#np.cumsum()

fig, ax = plt.subplots(2, 1  )



plt.show()


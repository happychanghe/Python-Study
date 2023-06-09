import math as m

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import Animation


def beta_pdf(x, a, n):
    _yn = np.zeros(len(x))

    for i in range(0, n+1):
        # print(type(_yn))
        _i=i%4
        if _i==1:
            _yn = _yn + np.cos(a)*np.power(x-a, i)/m.factorial(i)         # why error when using += ??
        elif _i==2:
            _yn = _yn + -np.sin(a)*np.power(x-a, i)/m.factorial(i)
        elif _i==3:
            _yn = _yn + -np.cos(a)*np.power(x-a, i)/m.factorial(i)
        elif _i==0:
            _yn = _yn + np.sin(a)*np.power(x-a, i)/m.factorial(i)
        else: 
            print("err!!!!!!!!!!!!!")
            exit()

    return _yn


class UpdateDist:
    def __init__(self, ax):
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(-3*np.pi, 3*np.pi, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(-3*np.pi, 3*np.pi)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.grid(True)


    def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        y = beta_pdf(self.x, i/10, 15)
        self.line.set_data(self.x, y)
        return self.line,



fig, ax = plt.subplots()
ud = UpdateDist(ax)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
x = np.linspace(-3*np.pi, 3*np.pi, 200)
ax.plot(x, np.sin(x))
# ax.plot(x, beta_pdf(x, 0, 5))
# print(beta_pdf(x, 0, 3)==beta_pdf(x, 0, 5))
plt.show()
# anim.save(filename=f'./output/sinx_animation_order{n}.mp4')
# saveanim = Animation(anim)
# saveanim.save(filename=f'./output/sinx_animation_order{n}.mp4')
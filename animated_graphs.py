import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

%matplotlib notebook

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

f = np.linspace(0, 2*np.pi, 20)

ani = animation.FuncAnimation(fig, update, frames=f,
                              init_func=init, #blit=True,
                              repeat=True)
plt.show()
ani.save('test.mp4', writer=writer)
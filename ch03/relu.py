# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 1.0)
y = relu(x)
plt.plot(x, y)
plt.xlim(-6, 6)
plt.ylim(-1, 5)
plt.show()

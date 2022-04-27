# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
fig1, ax1 = plt.subplots(figsize = [10, 5])
ax1.plot(x, y)

plt.title('A plot of sin(x)', fontsize = 16)
plt.xlabel('x', fontsize = 16)
plt.ylabel('y', fontsize = 16)
plt.grid(True)

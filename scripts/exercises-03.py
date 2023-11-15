# -*- coding: utf-8 -*-
"""
Exercises 3: Visualizing Data in Python
(Software Carpentry -- Shern Tee)
"""

# %% KEYBOARD SHORTCUTS

# F5:          Run Entire File
# Ctrl+Enter:  Run Current Cell
# Shift+Enter: Run Current Cell, Move Cursor To Next Cell
# F9:          Run Current Line or Highlighted Selection

# %% Playing with subplots!

# Here's the code for our previous subplots:

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')

fig, ax = plt.subplots(1, 3, figsize=(10.0, 3.0))
ax1, ax2, ax3 = ax

ax1.set_ylabel('average')
ax1.plot(np.mean(data, axis=0))

ax2.set_ylabel('max')
ax2.plot(np.amax(data, axis=0))

ax3.set_ylabel('min')
ax3.plot(np.amin(data, axis=0))

fig.tight_layout()

plt.savefig('inflammation1.png')
plt.show()

# Try swapping in these lines to test some formatting options:

# ax1.plot(np.mean(data, axis=0), color='blue', marker='o')
# ax1.plot(np.mean(data, axis=0), linestyle='dashed', linewidth=2)
# ax1.plot(np.mean(data, axis=0), 'g^', linestyle='none')
# ax1.plot(np.mean(data, axis=0), 'bo')
# ax1.plot(np.mean(data, axis=0), 'r+')

# %% Playing with stacked plots!

fig, ax = plt.subplots()

ax.plot(np.mean(data, axis=0), label='mean')
ax.plot(np.amax(data, axis=0), label='max')
ax.plot(np.amin(data, axis=0), label='min')
ax.legend()

plt.savefig('inflammation2.png')
plt.show()

# Try some formatting options! (See the previous cell for some ideas)
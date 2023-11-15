# -*- coding: utf-8 -*-
"""
Exercises 2: Loading Data into Python
(Software Carpentry -- Shern Tee)
"""

# %% KEYBOARD SHORTCUTS

# F5:          Run Entire File
# Ctrl+Enter:  Run Current Cell
# Shift+Enter: Run Current Cell, Move Cursor To Next Cell
# F9:          Run Current Line or Highlighted Selection

# %% More practice slicing arrays

# Let's import np. and create an array:
# You need commas between entries when _creating_ the array
# This is slightly different from when an array is _printed_
# (the commas are left out)
    
import numpy as np

array1 = np.array(
    [[1., 3., 5.],
     [2., 4., 6.]]
    )

# What do the following lines print out?

print(array1[0, 1])
print(array1[:, 2])
print(array1[1, :])
print(np.mean(array1, axis=0))
print(np.amax(array1, axis=1))

# Write your own operation to slice "array1"!

# %% Slicing strings

# In Python you can also slice _strings_, not just arrays.
# You may find this useful in particular fields (like 
# analysing a genetic sequence), but it's a useful exercise
# to get a better handle on slicing. Let's assign a string variable:

element = 'oxygen'

# What do the following lines print out?

print(element[0:3])
print(element[3:6])
print(element[4:])
print(element[:])
print(element[-1])
print(element[1:-1])

# Write your own operation to slice "element"!

# %% Differencing and accumulating

# We can get the data for patient 3 over week 1 as follows:

data = np.loadtxt(fname='../data/inflammation-01.csv', delimiter=',');
patient3_week1 = data[3, :7]
print(patient3_week1)

# The "np.diff" function calculates the difference
# between successive values in an array. Look at what
# the following line prints out, and try to understand it!

print(np.diff(patient3_week1))

# What about "np.cumsum" -- can you work out what it does?

print(np.cumsum(patient3_week1))

# Challenge: try applying either np.diff or np.cumsum
# to the entire "data" array. You may need the "axis" keyword.
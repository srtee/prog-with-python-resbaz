# -*- coding: utf-8 -*-
"""
Exercises 1: Python Fundamentals
(Software Carpentry -- Shern Tee)
"""

# %% KEYBOARD SHORTCUTS

# F5:          Run Entire File
# Ctrl+Enter:  Run Current Cell
# Shift+Enter: Run Current Cell, Move Cursor To Next Cell
# F9:          Run Current Line or Highlighted Selection

# %% A first go at variables! ('Check Your Understanding')

# What values do the variables mass and age have after each of the following statements? Test your answer by executing the lines.

mass = 47.5
age = 122
mass = mass * 2.0
age = age - 20

# Write more lines to change these variables!

# %% Multiple assignments ('Sorting Out References')

# In Python, you can assign multiple variables at once with commas.
# After this line, what are the values of "first" and "second"?

first, second = 'Grace', 'Hopper'

# And what will the "print" function print out?

third, fourth = second, first
print(third, fourth)

# Try your own multiple assignment!

# %% Seeing data types

# What are the data types of the following variables?

planet = 'Earth'
apples = 5
distance = 10.5

# %% F-strings

# "F-strings" are a killer feature in Python. When you write
# a string with the letter 'f' before it, Python will replace every
# variable between curly brackets { } with its value, and even run
# calculations or functions inside the brackets!

pi = 3.1415928
print(f'The value of PI is {pi}.')
print(f'And pi divided by three is {pi/3}.')

# You can supply format strings to get Python to format numbers nicely.
# See if you can work out the formatting language!

print(f'Pi is roughly {pi:.1f}.')
print(f'Pi times two million is {pi*2000000:,}.')
print(f'Pi times a trillion is {pi*(10 ** 9):.5g}.')
print(f'Here is a key line pi: {pi:=^30}.')
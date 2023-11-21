# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:42:57 2023

@author: uqstee4
"""

# function in a function

def add(x, y):
    """
    Adds two numbers

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return x+y

print(add(1,2))

# Generating docstrings:
# go to the colon and hit enter,
# then add three quotes (""")
# You should have an option to "generate docstring"

# %% function in a function

def addone(x, y):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    def add_just_one(x):
        return x+1
    return add_just_one(x)+y

print(addone(1,2)) # returns (1+1)+2

# %%

# print(add_just_one(1)) # oops, an error
# we can only use "add_just_one" inside addone

# %% This cell shows you that you can use other functions
# inside functions

def minus_just_one(x):
    return x-1

def minusone(x, y):
    return minus_just_one(x) + y

print(minusone(1,2))
print(minus_just_one(1))
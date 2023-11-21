# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def good_morning(name):
    print("Good morning,", name)

good_morning('wqepi')

def good_morning_string(name):
    return_string = "Good morning, " + name
    return return_string

def first_letter(s):
    return s[0]

greeting = first_letter(good_morning_string('Shern'))

# %% Multiple arguments

def greeting_and_time(name, time):
    s = "Good " + time + ", " + name
    return s

variable1 = greeting_and_time("Shern", "morning")
variable2 = greeting_and_time("Shern", "evening")
variable3 = greeting_and_time("Shern")

# positional argument: does not have a default value,
# so Python fills it out _by order_

# %% Default value

def greeting_with_default(name, time="morning"):
    s = "Good " + time + ", " + name
    return s

variable3 = greeting_with_default("Shern")

# default argument: now Python has a default
# and doesn't need an explicit value

# %% All default values!

def greeting_with_all_defaults(name="Shern", time="morning"):
    s = "Good " + time + ", " + name
    return s

variable4 = greeting_with_all_defaults()

# a function with all defaults can be run
# with NO parameters / arguments!

# %% Arguments by name

variable5 = greeting_with_all_defaults(time="evening", name="Amanda")

# if you give Python the _name_ of a parameter
# it doesn't have to guess by position

# %% A practical example

import numpy as np
import matplotlib.pyplot as plt

def plot_my_csv(input_filename, output_filename="None"):
    data = np.loadtxt(fname=input_filename, delimiter=',')
    
    fig, ax = plt.subplots()

    ax.plot(np.mean(data, axis=0), label='mean')
    ax.plot(np.amax(data, axis=0), label='max')
    ax.plot(np.amin(data, axis=0), label='min')
    ax.legend()
    
    ax.set_title(input_filename)

    plt.show()
    if (output_filename != "None"):
        plt.savefig(output_filename)

# %% apply the function
plot_my_csv("../data/inflammation-02.csv", "graph2.png")



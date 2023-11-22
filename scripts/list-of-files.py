# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:53:33 2023

@author: uqstee4
"""

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
plot_my_csv("../data/inflammation-02.csv") # output_filename is "None"
# so "savefig" line won't run

plot_my_csv("../data/inflammation-02.csv","my-graph-number-2.png")
# now output_filename is "my-graph-number-2.png"
# so "savefig" will run

plot_my_csv(output_filename="graph3.png",input_filename="../data/inflammation-03.csv")
# once there is one named argument
# you cannot mix in "positional" arguments (arguments with no default)

# %% get a list of file names

import glob

filelist = glob.glob("../data/inf*.csv")
# get all files matching "../data/inf{ANY PATTERN, INCLUDING NO CHARACTERS}.csv"

print(filelist)

# %% repeat operation for list of file names

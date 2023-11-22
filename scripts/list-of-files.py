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

filelist2= glob.glob("../data/*.csv")
print(filelist2)

# %% repeat operation for list of file names

for file in filelist:
    # now the variable "file" inside this loop
    # will be each of the "filelist" entries
    # one by one
    print(file)
    print("this was an entry")
    
# %% make all plots!!

# please clear plot window first for maximum fun

for file in filelist:
    plot_my_csv(file)
    
# %% variation 1: save graph to output PNGs

for file in filelist:
    plot_my_csv(file, file+"-output.png")
    
# for example file "../data/inflammation-01.csv"
# output will be "../data/inflammation-01.csv-output.png"

# %% variation 2: enumerate

for number, file in enumerate(filelist):
    print(number, file)
# enumerate will give you both the list entry
# and its number

# %% save graphs with properly numbered output PNGs

#for number, file in enumerate(filelist):
#    plot_my_csv(file, "output"+(number+1)+".png")

# for example file "../data/inflammation-01.csv"
# number will be 0, (number+1) will be 1
# output will be "output1.png"
# but this version doesn't work because
# "number+1" is still a number, not a string

for number, file in enumerate(filelist):
    plot_my_csv(file, "output"+str(number+1)+".png")
    
# "str" changes number to string

# %% enumerate start from 1 with fixed string length

for number, file in enumerate(filelist, 1):
    print(f'{number:02}', file)
    
# enumerate(LIST, x) makes the first entry x
# f'{number:02}' makes it output as a string of length *2*,
# with "0s" for left-padding

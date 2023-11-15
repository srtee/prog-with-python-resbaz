# -*- coding: utf-8 -*-
"""
Exercises 4: Visualizing Data in Python
(Software Carpentry -- Shern Tee)
"""

# %% Slicing from the end

# Write some Python code to print only the last four characters
# of "string_for_slicing", or the last four entries (both element
# name and abbreviation) of "list_for_slicing".

string_for_slicing = 'Observation date: 02-Feb-2013'
list_for_slicing = [['fluorine', 'F'],
                    ['chlorine', 'Cl'],
                    ['bromine', 'Br'],
                    ['iodine', 'I'],
                    ['astatine', 'At']]

# Does your solution still work if we change the list length?

another_list     = [['fluorine', 'F'],
                    ['chlorine', 'Cl'],
                    ['bromine', 'Br'],
                    ['iodine', 'I'],
                    ['astatine', 'At'],
                    ['carbon', 'C'],
                    ['oxygen', 'O']]

# %% Non-continuous slices

# You can put in a _third_ argument to the "slice" (square brackets)
# called the "step size". Run the code below. What does it do?

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset1 = primes[0:12:3]
print('subset 1:', subset1)

# And what does this code do?

subset2 = primes[2:12:3]
print('subset 2:', subset2)

# Slice the "Beatles" string below
# to get the output "I notpssgre ntesae":
    
beatles = "In an octopus's garden in the shade"

# print(beatles[?:?:?])

# %% Overloaded list operators

# Run the code below:

import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9, 10]

array1 = np.array(list1)
array2 = np.array(list2)
array3 = np.array(list3)

# You might have to run some of the following lines individually
# to skip some errors! Remember how to do that?

print(list1 + list2)
print(array1 + array2)
print(list1 * 2)
print(array1 * 2)
print(list1 + list2 + list3)
print(array1 + array2 + array3)

# Challenge: combine list1, list2, and list3 together
# to get the printout:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



# (Hint: try writing a list slice with default start, default end,
# and a step size of -1.)

# %% Appending, extending, inserting, removing

# Python has many ways to manipulate lists. Run the code below to see
# how they work! Make sure you change some values to really understand.

my_fav_things = ["raindrops"]

my_fav_things.append("roses")
print("Appended:", my_fav_things)
my_fav_things.append(["whiskers", "kittens"])
print("Appended:", my_fav_things)
my_fav_things.extend(["kettles", "mittens"])
print("Extended:", my_fav_things)
my_fav_things = my_fav_things + ["brown paper packages"]
print("Add:", my_fav_things)
my_fav_things = my_fav_things + ["tied up", "in strings"]
print("Add:", my_fav_things)
my_fav_things.insert(3, "a mystery gift!")
print("Inserted:", my_fav_things)
my_fav_things.insert(3, ["ponies", "strudels"])
print("Inserted:", my_fav_things)
my_fav_things.remove("roses")
print("Removed:", my_fav_things)
my_fav_things.remove("slugs")
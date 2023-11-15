# -*- coding: utf-8 -*-
"""
Exercises 6: Loops and Iterations
(Software Carpentry -- Shern Tee)
"""

# %% The range() function

# Experiment with the following loops to work out
# what range() does. (Replace the question marks with numbers!)

# for n in range(?):
#   print n

# for n in range(?,?):
#   print n

# Use range-loops to print out 1, 2, and 3 (on successive lines).
# How about 0.5, 1.0, 1.5?

# Challenge: Try print(range(1000)). What do you see? Why might this
# be helpful for efficient calculations?

# %% Summing with a list

# Write some Python code to sum up the values of a list.
# For example, your code should print out "562" for the list below:

numbers = [124, 402, 36]






# Change the entries of "numbers" and make sure your code works!

# %% Enumerate

# The _enumerate_ function returns both an item's position in the list
# and the item itself. These are often called "idx" and "val" in generic
# code. Run the code below and try to understand "enumerate":

for idx, val in enumerate(['apple', 'bear', 'cat']):
    print ("List entry", idx, "is the word:", val)

# %% Nested loops

# You can put one loop inside another. For example:

for i in range(4):
    for j in range(i):
        print(f'This is run {i} of the outer loop and run {j} of the inner loop')

# What does range(0) do?

# %% Enumerating Christmas

# Let's teach Python a Christmas carol! Starting from the list below,
# get Python to print the Twelve Days of Christmas. Since Python doesn't
# know much about English, we'll be happy to see something like:

# On Day 1 of Christmas, my true love gave to me
# a partridge in a pear tree
# On Day 2 of Christmas, my true love gave to me
# two french hens
# a partridge in a pear tree
# ...

true_love_gifts = [
    "a partridge in a pear tree",
    "two turtle doves",
    "three french hens",
    "four calling birds",
    "fiiiive golden riiiings",
    "six geese a-laying",
    "seven swans a-swimming",
    "eight maids a-milking",
    "nine ladies dancing",
    "ten lords a-leaping",
    "eleven pipers piping",
    "twelve drummers drumming"]
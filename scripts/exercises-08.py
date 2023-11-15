# -*- coding: utf-8 -*-
"""
Exercises 8: Functions
(Software Carpentry -- Shern Tee)
"""

# %% A Wrapper Function

# Write a function that takes two parameters, "original" and "wrapper",
# and returns a new string that has the original string with the wrapper
# added to both sides. For example:
# print(fence("name", "*"))
# output: *name*

# %% Return vs print

# Run the code below, and figure out what happens.

def add(a, b):
    print(a + b)

A = add(7, 3)
print(A)

# %% Write a rescale function

# Write a function rescale that takes an array as input 
# and returns a corresponding array of values scaled 
# to lie in the range 0.0 to 1.0. (Hint: If L and H 
# are the lowest and highest values in the original array, 
# then the replacement for a value v should be (v-L) / (H-L).)

# %% Default and non-default parameters

# Run the following code and work out how Python deals with
# default and non-default parameters.

def numbers(num1, num2 = 2, num3, num4 = 4):
    return f'{num1}  {num2}  {num3}  {num4}'

print(numbers(1, num3 = 3))

# %% Ho Ho Ho! It's a Functional Christmas!

# The code below gets Python to print the lyrics of Twelve Days of Christmas.
# Try writing a function -- with docstring! -- to make the code more readable.

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

day_of_christmas = "day of Christmas, my true love gave to me"

for i in range(12):
    if i == 0:
        print('On the 1st', day_of_christmas)
    elif i == 1:
        print('On the 2nd', day_of_christmas)
    elif i == 2:
        print('On the 3rd', day_of_christmas)
    else:
        print(f'On the {i+1}th', day_of_christmas)
    for j, gift in enumerate(true_love_gifts[i::-1]):
        if j == i and i > 0:
            print('and', gift)
        else:
            print(gift)
    if i != 11:
        print('')
        print('(next verse:)')
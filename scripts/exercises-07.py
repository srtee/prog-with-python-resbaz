# -*- coding: utf-8 -*-
"""
Exercises 7: Making Choices
(Software Carpentry -- Shern Tee)
"""

# %% Tracing logic

# Imagine using ifs and elifs to mark a student's answers:

answers = [3, 4, 1]

# Run this code:

if answers[0] == 3:
    print('Answer 1 correct!')
elif answers[1] == 4:
    print('Answer 2 correct!')
elif answers[2] == 2:
    print('Answer 3 correct!')

# And then run this code:

if answers[0] == 3:
    print('Answer 1 correct!')
elif answers[1] == 4:
    print('Answer 2 correct!')
elif answers[2] == 2:
    print('Answer 3 correct!')

# What's the difference?

# %% "What is truth"?

# Python can use _any_ value to make decisions in if and elif,
# not just the special Boolean values true and false. Work out
# Python's rules from the code below:

if '':
    print('empty string is true')
if 'word':
    print('word is true')
if []:
    print('empty list is true')
if [1, 2, 3]:
    print('non-empty list is true')
if 0:
    print('zero is true')
if 1:
    print('one is true')

# %% Sorting things into buckets

# Pythons (the snakes) like eating small animals. Python (the
# programming language) doesn't know what animals are large or small,
# but it can decide if animals have large or small names. Sort the
# animal names below into "large_names" (six letters or longer) and
# "small_names" (fewer than six letters).

animal_names = ["fox", "elephant", "bat", "dog", "tyrannosaurus", "tardigrade"]

# Hint: try starting with the code below

large_names = []
small_names = []

for name in animal_names:
    large_names.append(name) # oh no, we need to make some choices here

print("Large names:", large_names)
print("Small names:", small_names)

# %% Ordinal numbers

# Let's teach Python some English! We state the order of things in a
# sequence with ordinal numbers: 1st, 2nd, 3rd, 4th, 5th, 6th, ...
# Fix the code below to write ordinal numbers!

for i in range(1,10):
    print(f'Number {i} has the ordinal form {i}st.') # oops?

# %% Challenge: Christmas Time, Round Two!

# Use ifs and elifs to teach Python the proper version of
# Twelve Days of Christmas:

# On the 1st day of Christmas, my true love gave to me
# a partridge in a pear tree
# On the 2nd day of Christmas, my true love gave to me
# two french hens
# and a partridge in a pear tree
# On the 3rd day of Christmas ...

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
# Make two simple histograms

# Create a histogram from a given list of integers
# Question! Write an app to get a space separated list and make a histogram
# First, without list comprehentions
# items = [int(c) for c in input('list: ').split(" ") if c.isnumeric()]
# for i in items:
#     print(("■︁") * i)


# Write a Python program to count the number of characters (character frequency) in a string and make a histogram
string = input('please enter your text: ')
result = {} # empty curly brackets are dictiories not sets
for char in string:
    if char == " ": continue
    result[char] = 1 if char not in result else result[char] + 1

for c in result: print(c, "■︁" * result[c], result[c])

# TIPs
# list comprehention
# .split()
# .isnumeric()
# continue
# "in" keyword
# one line loop
# one line if
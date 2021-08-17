# Create a histogram from a given list of integers
# Question! Write an app to get a space separated list and make a histogram
# First, without list comprehentions
items = [int(c) for c in input('list: ').split(" ") if c.isnumeric()]
for i in items:
    print(("■︁") * i)


# Write a Python program to count the number of characters (character frequency) in a string and make a histogram
string = input('please enter your text: ')
result = {}
for char in string:
    if char == " ": continue
    if char not in result:
        result.update({char: 0})
    result[char] += 1

for c in result: print(c, "■︁" * result[c], result[c])

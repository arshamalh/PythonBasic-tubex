# Make two simple histogram drawer apps

# Write an app to get a space separated list and make a histogram just in one line!
for i in input('Enter space separated values: ').split(" "): print(("■︁") * int(i)) if i.isnumeric() else ""

# Write a Python program to count the number of characters (character frequency) in a string and make a histogram
string = input('please enter your text: ').replace(" ", "")
result = {} # empty curly brackets are dictiories not sets
for char in string: result[char] = 1 if char not in result else result[char] + 1
for c in result: print(c, "■︁" * result[c], result[c])

# TIPs
# list comprehention
# .split()
# .isnumeric()
# continue
# "in" keyword
# one line loop
# one line if
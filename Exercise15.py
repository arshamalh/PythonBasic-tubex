"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

def staend(inplist):
    newlist = [inplist[0], inplist[len(inplist) - 1]]
    return newlist


print(staend([2, 3, 5, 7, 8, 12]))
mylist = [2, 4, 6, 8, 2, 3]
myset = set(mylist)
nli = list(myset)
print(nli)

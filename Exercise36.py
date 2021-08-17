# Write a Python program to check whether a specified value is contained in a group of values.
checking_value = int(input('> '))
items = [int(c) for c in list(input('> ')) if c.isnumeric()]
print(checking_value in items)


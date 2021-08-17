# Create a histogram from a given list of integers
items = [int(c) for c in input('list: ').split(" ") if c.isnumeric()]
for i in items:
    print(("■︁") * i)

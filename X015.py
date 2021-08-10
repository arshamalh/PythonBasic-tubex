# Create a histogram from a given list of integers
items = [int(c) for c in list(input('list: ')) if c.isnumeric()]
character = input('character: ')
for i in items:
    print(character * i)

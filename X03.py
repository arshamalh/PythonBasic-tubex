# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
def sorter(seq):
    list_of_items = [item.strip() for item in seq.split(',')]
    list_of_items.sort()
    return list_of_items

print(sorter('black, green, blue, red, yellow, violet, purple, white, pink'))

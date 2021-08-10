# Write a Python program to count the number of characters (character frequency) in a string.
string = input('please enter your text: ')
result = {}
for character in string:
    if character not in result:
        result.update({character: 0})
    result[character] += 1

print(result)



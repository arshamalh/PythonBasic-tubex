# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

"""
11.	What does name.strip() do?
5.	What happens when we prefix a parameter with an asterisk (*)?
6.	What about two asterisks (**)?
"""

# Input a number, if it is not a number generate an error message
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()

# complex list comprehension with conditions and some loop
x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b % 2 != 0]

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = [even for even in a if even % 2 != 0]
print(evens)

# Write a Python program to check whether a specified value is contained in a group of values.
checking_value = int(input('> '))
items = [int(c) for c in list(input('> ')) if c.isnumeric()]
print(checking_value in items)

# Compute the digit number of sum of two given integers
# Make a tutorial about map and filter
a, b = map(int, input("Input two integers(a b): ").split(" "))
print("Number of digit of a and b:", len(str(a+b)))

# create a random list
# This line of code will leave a containing a list of 5 random numbers from 0 to 9
import random
a = random.sample(range(10), 5)

import random
a = random.sample(range(10), random.randint(1, 10))
b = random.sample(range(10), random.randint(1, 10))
result = list(dict.fromkeys([num_a for num_a in a for num_b in b if num_a == num_b]))
print(f'A: {a}')
print(f'B: {b}')
print(f'Result: {result}')

# Concatenate N strings
list_of_colors = ['Red', 'White', 'Black']
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()

# Display a floating number in specified numbers
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()

# Check whether lowercase letters exist in a string
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))

# Convert an integer to binary keep leading zeros
x = 12
print(format(x, '08b'))
print(format(x, '010b'))

# Convert decimal to hexadecimal
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))

# duplicate remover:
import random
SampleList = [random.randint(1, 9) for _ in range(1, 20)] # It will have at least twice of any number
def DuplicateRemover(GivenList):
    result = []
    for x in GivenList:
        if x not in result: result.append(x)
    return result
print(f'Sample is :{SampleList}')
print(f'Result is :{DuplicateRemover(SampleList)}')
# easier way:
SampleList = list(dict.fromkeys(SampleList))
print(SampleList)


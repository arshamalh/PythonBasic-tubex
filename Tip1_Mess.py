"""
11.	What does name.strip() do?
5.	What happens when we prefix a parameter with an asterisk (*)?
6.	What about two asterisks (**)?
"""

# Get the details of math module
import math
math_ls = dir(math)
print(math_ls)

# Find the available built-in modules
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=60))

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

# duplicate remover:
"""
print(result)
for x in result:
    detect = result.count(x)
    if detect > 1:
        i = 0
        while i < detect - 1:
            result.remove(x)
            print(i)
            i += 1
print(f'Result is :{result}')
# easier way:
result = list(dict.fromkeys(result))
print(result)
"""

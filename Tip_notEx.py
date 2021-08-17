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
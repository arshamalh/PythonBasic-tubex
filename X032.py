# Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
from PythonExercise1.Exercise23 import factorial
def zero_separator(number):
    number = factorial(number)
    print(number)
    n_o_digits = 0
    while number % 10 == 0:
        number //= 10
        n_o_digits += 1

    print(n_o_digits)

zero_separator(int(input('> ')))

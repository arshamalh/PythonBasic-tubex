"""
we have a 3 digit number like 123 that we called that abc
show numbers that satisfy the condition below:
a^2 + b^2 + c^2 = abc
"""
from PythonExercise1.Exercise23 import factorial
for x in range(100, 1000):
    li_x = [int(a) for a in str(x)]
    if factorial(li_x[0]) + factorial(li_x[1]) + factorial(li_x[2]) == x:
        print(x)

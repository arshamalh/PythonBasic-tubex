# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""
(6, 9)
(24, 8)
(125, 225)
(16, 12)
"""
"""
first, we have to find the smaller number and GCD can't be greater than that
second, we have to loop till that
"""
num_1 = int(input('num 1: '))
num_2 = int(input('num 2: '))
smaller = num_1 if num_1 < num_2 else num_2
greater = num_2 if num_1 < num_2 else num_1
del num_1, num_2
GCD = smaller
while GCD > 0 and greater % smaller != 0:
    GCD -= 1
    if smaller % GCD == 0 and greater % GCD == 0:
        break

print(GCD)

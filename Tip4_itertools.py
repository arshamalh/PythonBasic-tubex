# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
# TODO: Make a full tutorial around itertools
from itertools import permutations
pers = permutations(['a', 'e', 'i', 'o', 'u'], 5)
for item in pers:
    print(''.join(item))

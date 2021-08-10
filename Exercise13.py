# complex list comprehension with conditions and some loop
x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b % 2 != 0]

# create a random list
# This line of code will leave a containing a list of 5 random numbers from 0 to 9
import random
a = random.sample(range(10), 5)

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

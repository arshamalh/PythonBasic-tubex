import random
a = [random.randint(1, 10) for _ in range(1, 10)]
b = [random.randint(1, 10) for _ in range(1, 10)]
result = [num_a for num_a in a if num_a in b]
print(f'Array1:{a}', f'Array2:{b}', f'Unarranged list: {result}',  sep="\n")
print(f'Result is :{sorted(list(set(result)))}')

# Refactoring
# Making random list
# Finding intersections
# Duplication Remover
# But before that, we want to show you what this app is made for and how it works
# It's so helpful and has a lot of tricks
# this app makes two random lists and find the intersection of them

# We got array 1 and array 2 as random lists and unarranged result
# unarranged list is the one which is not ordered and have duplicated values (for example four times six and three times 2)
# And as intersection means, any number in unarranged list has to be in both of lists. (for exmaple 1 and 3 are only in the array 2)

# TODO: Before we go to the exercise, first decrease the lines of code without destroying the functionality (Pause and think part)
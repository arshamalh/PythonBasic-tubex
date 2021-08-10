a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = [even for even in a if even % 2 != 0]
print(evens)

# also for a random list with a random size
import random
numlist = []
list_length = random.randint(5, 15)
while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))

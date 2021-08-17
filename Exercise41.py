import random
a = random.sample(range(10), random.randint(1, 10))
b = random.sample(range(10), random.randint(1, 10))
result = list(dict.fromkeys([num_a for num_a in a for num_b in b if num_a == num_b]))
print(f'A: {a}')
print(f'B: {b}')
print(f'Result: {result}')
import random
a = [random.randint(1, 10) for _ in range(1, 10)]
b = [random.randint(1, 10) for _ in range(1, 10)]
result = [num_a for num_a in a if num_a in b]
print(f'Array1:{a}', f'Array2:{b}', f'Unarranged list: {result}', sep='\n')
print(f'Result is :{sorted(list(set(result)))}')
# Humans have to improve themselves... :)

# Random list with a random size (Not this example, but interesting!)
import random
numlist = [random.randint(1, 75) for _ in range(random.randint(5, 15))]
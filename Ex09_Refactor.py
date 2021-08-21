import random
a = []
b = []
for i in range(1, 10):
    a.append(random.randint(1, 10))
    b.append(random.randint(1, 10))
print(f'Array1:{a}')
print(f'Array2:{b}')

# Intersection list
result = []
for num_a in a:
    for num_b in b:
        if num_a == num_b:
            result.append(num_a)

print('Unarranged list: ', result)
# Duplicate remover
for x in result:
    detect = result.count(x)
    if detect > 1:
        i = 0
        while i < detect - 1:
            result.remove(x)
            i += 1

# Sorter
for i in range(len(result)):
    for j in range(len(result)):
        if result[j] > result[i]:
            temp = result[j]
            result[j] = result[i]
            result[i] = temp

print(f'Result is :{result}')

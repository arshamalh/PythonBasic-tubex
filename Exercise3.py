def even_odd(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield "Even " + str(i)
        else:
            yield "Odd  " + str(i)


number = int(input('please enter a number: '))
result = even_odd(number)
for item in result:
    print(item)

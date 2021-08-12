def evenOdd(number):
    for i in range(1, number + 1): # 18 
        if i % 2 == 0:
            yield "Even : " + str(i)
        else:
            yield "Odd  : " + str(i)


number = int(input("Give me the number: "))
for item in evenOdd(number):
    print(item)



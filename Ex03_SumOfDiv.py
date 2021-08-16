# Write a program to calculate the summation of all numbers before a limitation which are divisible by 3 or 7
def SumDiv(limit, number_1=3, number_2=7):
    sum = 0
    for i in range(limit):
        if i % number_1 == 0 or i % number_2 == 0:
            sum += i # sum = sum + i
    return sum

lim = int(input("What is your limit? "))
print(f'Sumation is: {SumDiv(lim)}')


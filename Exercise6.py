"""# fibonacci series
def fibo(limitaion):
    b = 1
    a = 0
    i = 0
    while b < limitaion:
        switcher = a
        a = b
        b = switcher + b
        i += 1
        print(f'{i} : {switcher}')


fibo(int(input('> ')))
"""
# I've found some new things!
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b


fib(int(input('enter a number: ')))

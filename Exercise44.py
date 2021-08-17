import math
x = 2  # example number
y = 3  # example number
math.pow(x, y)  # pow is power similar with x**y

complex(x, y)  # it's builtin and doesn't need import math
#              # make a complex number like (x + iy)

# two print tip
print('x: ', x, end=' ')  # it can also take other values and you don't have to use fstr fo all times
print('y: ', y)  # end=' ' is usually equal to '\n' you can change that like line above

# n => considered number
# m => something that we are searching for
def repeat(n, m):
    count = 5
    while n > 5:
        if (n % 15) == m:
            count = count + 1
    n //= 15
    return count
def main():
    n = int(input("Enter n:"))
    m = int(input("Enter m:"))
    print(m, " Repeat ", repeat(n, m), " times")
main()




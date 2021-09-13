# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

def factorial(n):
    if n < 0: raise ValueError("Can't pass negative values to factorial")
    if n == 0: return 1 # 0! == 1
    fac = 1
    for i in range(1, n + 1): # we write n + 1 here because n + 1 itself is not included and n is included
        fac *= i # fac = fac * i
    return fac

print(factorial(int(input("Enter a positive number: "))))

# 1 * 1
# 1 * 2
# 2 * 3
# 6 * 4
# 1 * 2 * 3 * 4
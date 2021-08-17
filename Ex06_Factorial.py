def factorial(n):
    if n == 0: # 0! == 1
        fac = 1
    else:
        fac = 1
        for i in range(1, n+1): # n+1 is not included in range, n is included and we want it
            fac *= i # fac = fac * i
    return fac


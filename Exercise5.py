# prime number
def Pnum(lim):
    for i in range(1, int(lim)):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


number = input('enter your limitation: ')
print(list(Pnum(number)))

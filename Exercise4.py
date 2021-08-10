def sp_sum(limitation):
    summation = 0
    for i in range(int(limitation)):
        if i % 3 == 0 or i % 5 == 0:
            summation += i
    return summation


lim = input("enter your limitation: ")
print(f'Sumation is: {sp_sum(lim)}')


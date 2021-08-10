def fizz_buzz(p_num):
    p_num = int(p_num)
    if p_num % 3 == 0 and p_num % 5 != 0:
        return 'fizz'
    elif p_num % 5 == 0 and not p_num % 3 == 0:
        return 'buzz'
    elif p_num % 3 == 0 and p_num % 5 == 0:
        return 'fizz-buzz'
    else:
        return p_num


num = input('enter a number to check fizz-buzz: ')
print(fizz_buzz(num))

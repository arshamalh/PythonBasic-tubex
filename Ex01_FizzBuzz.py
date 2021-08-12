# Creating a fizz buzz 

# A Fizz Buzz is an app which show you if a given number is 
# divisible by 3 or 5 or both or none

# So we have to write 4 conditions
# only by 3
# only by 5
# by 3 and 5
# by none of them

def fizz_buzz(p_num = 0):
    if p_num % 3 == 0 and p_num % 5 != 0:
        return 'fizz'
    elif p_num % 5 == 0 and not p_num % 3 == 0:
        return 'buzz'
    elif p_num % 3 == 0 and p_num % 5 == 0:
        return 'fizz-buzz'
    else:
        return p_num

num = int(input('enter a number to check fizz-buzz: '))
print(fizz_buzz(num))

# % is the modulus operator which give us the reminder
# 5 % 2 = 1
# 7 % 3 = 1
# 8 % 2 = 0 => 8 is divisible by 2
# 9 % 3 = 0 => ----

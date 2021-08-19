# Palindrome
user_st = input("please enter your string: ").lower()
detector = True
for i in range(len(user_st) // 2 + 1):  # // => divide and cut the floats
    if user_st[i - 1] != user_st[-i]:   # [-index] count from the last
        detector = False                # detector is global and you can change it everywhere
        break

if detector:
    print(f'{user_st} is palindrome')
else:
    print(f'{user_st} is not a palindrome')

# another method:
# Something I love about Python is its shortcuts, you can do everything with least effort
# inp = input("Enter a word: ").lower()
# if inp == inp[::-1]: print("{inp} is a palindrome!")
# else: print("{inp} is not a palindrome!")

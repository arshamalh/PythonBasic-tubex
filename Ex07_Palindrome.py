# Palindrome
user_st = input("please enter your string: ").lower()
detector = True
for i in range(len(user_st) // 2 + 1):
    if user_st[i - 1] != user_st[-i]:
        detector = False
        break

if detector:
    print(f'{user_st} is palindrome')
else:
    print(f'{user_st} is not a palindrome')

# another method:
# inp = input("Enter a word: ").lower()
# if inp == inp[::-1]: print("{inp} is a palindrome!")
# else: print("{inp} is not a palindrome!")

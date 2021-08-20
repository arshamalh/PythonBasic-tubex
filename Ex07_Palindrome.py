# Palindrome
user_st = input("please enter your string: ").lower()
detector = True
for i in range(len(user_st) // 2):     # // => divide and cut the floats
    if user_st[i] != user_st[-(i+1)]:  # [-index] negative indexes start counting from the last
        detector = False               # detector is global and you can change it everywhere
        break

if detector: print(f'{user_st} is palindrome')
else: print(f'{user_st} is not a palindrome')

# another method:
# Something I love about Python is its shortcuts, you can do everything with least effort
inp = input("Enter a word: ").lower()
print("It's a palindrome") if inp == inp[::-1] else print("It's not a palindrome")

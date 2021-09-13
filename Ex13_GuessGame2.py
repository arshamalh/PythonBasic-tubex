# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed close, too far, or exactly right.
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
from random import randint
print('Enter "Exit" whenever you want')
guess = randint(1, 10)
mistakes = 0
while True:
    inp = input('Enter your guessing number between 1-9: ').lower()
    if inp[0] == 'e':
        print('I hope you enjoyed my program')
        print(f"you've got {mistakes} times mistakes")
        break
    else:
        inp = int(inp)
        if guess == inp:
            print('right choice')
            print(f"you've got {mistakes} times mistakes")
            break
        elif abs(guess - inp) > 3:
            print('your choice is too far')
            mistakes += 1
        elif abs(guess - inp) <= 3:
            print('your choice is close')
            mistakes += 1

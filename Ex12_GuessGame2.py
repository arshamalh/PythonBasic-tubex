"""
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."""
import random
c_random = random.randint(1000, 10000)
c_random = str(c_random)
u_guess = ''
print(c_random)
cow = 0
while cow != 4:
    u_guess = input('Make a guess: ')
    cow = 0
    bull = 0
    index = 0
    for x in u_guess:
        if x == c_random[index]:
            cow += 1
        for y in c_random:
            if x == y:
                bull += 1
        index += 1
    print(f'cow: {cow} \nbull: {bull - cow}')

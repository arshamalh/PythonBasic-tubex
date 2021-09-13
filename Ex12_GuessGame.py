# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

"""
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."""
import random
c_random = str(random.randint(1000, 10000))
bull, cow = 0, 0
while cow != 4:
    u_guess = input('Make a guess: ').strip()[0:4]
    if not u_guess.isnumeric(): 
        print("Make a numeric guess!")
        continue
    
    for index, x in enumerate(u_guess):
        if x == c_random[index]: # if x equals its corresponding item in random generated object
            cow += 1 
            continue
        # if we pass the previous condition,
        # it means x is not in the right place and if it's in the c_random,
        # we can count it.
        if x in c_random: bull += 1

    print(f'cow: {cow} \nbull: {bull}')

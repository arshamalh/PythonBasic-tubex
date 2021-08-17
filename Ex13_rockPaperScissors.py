# Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game
from random import choice
print("""
Welcome to my program, program will start automatically
if you want to stop, just type 'stop'
if you want to play again from zero, just type 'restart'
and you want to play, just type your chance of rock, paper, scissors (or r, p, s)
""")
states = ['r', 'p', 's']
c_wins = 0
u_wins = 0
c_choice = ''
while True:
    inp = input("> ").lower()
    c_choice = choice(states)
    if inp == 'stop':
        print('thank you for using my app')
        break
    elif inp == 'restart':
        c_wins = 0
        u_wins = 0
        c_choice = ''
    elif inp[0] == 'r':
        if c_choice == 'p':
            c_wins += 1
        elif c_choice == 's':
            u_wins += 1
    elif inp[0] == 'p':
        if c_choice == 's':
            c_wins += 1
        elif c_choice == 'r':
            u_wins += 1
    elif inp[0] == 's':
        if c_choice == 'r':
            c_wins += 1
        elif c_choice == 'p':
            u_wins += 1
    print(f' User Wins: {u_wins} \n Computer Wins: {c_wins} \n Computer Choice was: {c_choice}')


# also for a random list with a random size
import random
numlist = []
list_length = random.randint(5, 15)
while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))


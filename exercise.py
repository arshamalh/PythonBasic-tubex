# Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game

from random import choice
from ColorText import color
u_wins, c_wins = 0, 0
print("""
Welcome to RPS game
You can start playing by typing your chance of rock, paper, scissors (or r, p, s)
if you want to exit, just type 'exit'
if you want to play again from zero, just type 'again'
""")

Shaper = {"r": "💎︁",
          "p": "📜︁",
          "s": "✀︁"}

while True: 
    c_choice = choice(['r', 'p', 's'])
    inp = input("> ").lower()[0] 
    if inp == 'e':
        print("Thank you for playing with us!")
        break

    elif inp == "a":
        u_wins, c_wins = 0, 0
        print("Restarted!")
        continue

    # User wins
    elif (inp == 'r' and c_choice == 's'
    ) or (inp == 's' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 'r'): u_wins += 1

    elif (inp == 's' and c_choice == 'r'
    ) or (inp == 'r' and c_choice == 'p'
    ) or (inp == 'p' and c_choice == 's'): c_wins += 1

    else: continue

    print(f' User Wins: {color(50, 250, 50, u_wins)} \n Computer Wins: {color(250, 50, 50, c_wins)} \n You {Shaper[inp]}  vs {Shaper[c_choice]}  Computer')
        



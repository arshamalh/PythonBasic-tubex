# a password have to have LowerCase - UpperCase - Numbers and Symbols
import random
import string
def pass_generator():
    nol = random.randint(1, 9)  # number of lowercase
    nou = random.randint(1, 9)  # number of Uppercase
    non = random.randint(1, 9)  # number of Numbers
    nos = random.randint(1, 6)  # number of Symbols

    indexer = 0
    u_pass = []
    while indexer < nol + non + nos + nou:
        if random.randint(1, 4) == 1:
            u_pass.append(random.choice(string.ascii_lowercase))
        elif random.randint(1, 4) == 2:
            u_pass.append(random.choice(string.ascii_uppercase))
        elif random.randint(1, 4) == 3:
            u_pass.append(random.choice(string.digits))
        elif random.randint(1, 4) == 4:
            u_pass.append(random.choice(string.punctuation))
        indexer += 1
    return ''.join(u_pass)

print(pass_generator())

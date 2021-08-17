c_guess = 50
widedict = {}
lowest = 0
highest = 100
guess_counter = 0
while True:
    uin = input(f"my guess is {c_guess}, what's your opinion about? \n(VeryHigh(vh), High(h), True(t), Low(l), VeryLow(vl)\n> ").lower()
    if uin == 't':
        print('u are right!')
        break
    elif uin == 'vh' and c_guess not in widedict:
        widedict.update({c_guess: uin})
        highest = c_guess
        c_guess = (c_guess+lowest)//2
    elif uin == 'h' and c_guess not in widedict:
        widedict.update({c_guess: uin})
        highest = c_guess
        c_guess -= 2
    elif uin == 'l' and c_guess not in widedict:
        widedict.update({c_guess: uin})
        lowest = c_guess
        c_guess += 2
    elif uin == 'vl' and c_guess not in widedict:
        widedict.update({c_guess: uin})
        lowest = c_guess
        c_guess = (c_guess+highest)//2
    while c_guess in widedict and widedict[c_guess] == 'h':
        widedict.update({c_guess: uin})
        c_guess -= 1
    while c_guess in widedict and widedict[c_guess] == 'l':
        widedict.update({c_guess: uin})
        c_guess += 1
    guess_counter += 1
    print(f"you've made {guess_counter} times guess")
    print(widedict)


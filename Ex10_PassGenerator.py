# a password have to have LowerCase - UpperCase - Numbers and Symbols
import random
import string
def PassGenerator(lenP=0):
    def shortPass():
        u_pass = [random.choice(string.ascii_lowercase), 
                  random.choice(string.ascii_uppercase),
                  random.choice(string.digits), 
                  random.choice(string.punctuation)]

        random.shuffle(u_pass)
        return ''.join(u_pass)

    if lenP == 0: lenP = random.randint(8, 16)
    elif lenP < 4: return "Your password is totally unsafe"
    elif lenP == 4: return shortPass()
    
    Upass = []
    while len(Upass) < lenP: Upass.append(shortPass()[0])
    return ''.join(Upass)


print(PassGenerator())



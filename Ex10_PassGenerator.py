import random, string

def RandomChar(types="luns"):
    TypeValues = {
        "l": string.ascii_lowercase,
        "u": string.ascii_uppercase,
        "n": string.digits,
        "s": string.punctuation
    }
    return [random.choice(TypeValues[item]) for item in types if item in TypeValues]

def PassGenerator(LenP=0): # 0 stands for random length
    # RandomChar will get a string of characters needed and return a list of random characters.

    if LenP == 0: LenP = random.randint(8, 16)
    elif LenP == 4: return "".join(RandomChar())
    elif LenP < 4: raise ValueError("Your password is totally unsafe!")

    uPass = [RandomChar()[random.randint(0, 3)] for _ in range(LenP)]
    random.shuffle(uPass)
    return "".join(uPass)

print(PassGenerator())

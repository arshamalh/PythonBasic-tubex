# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

import random, string

def PassGenerator(LenP=0): # if we want to make argument optional, we have to pass a default value to it
    # Define letters
    TypeValues = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)

    # Custom or Random len
    if LenP == 0: LenP = random.randint(8, 16)
    elif LenP < 4: raise ValueError("Your password is totally unsafe!")

    # Making the list
    # Challange: if we get 8 as i, do we have 8 in TypeValues?
    uPass = [random.choice(TypeValues[i % 4]) for i in range(LenP)] 
    random.shuffle(uPass)
    
    return "".join(uPass)

print(PassGenerator())


# 1 => 1
# 2 => 2
# ...
# 5 => 1
# 6 => 2
# 7 => 3
# 8 => 4
# 9 => 1

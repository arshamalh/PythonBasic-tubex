import random, string
def PassGenerator(LenP=0): # if we want to make argument optional, we have to pass a default value to it
    # Define letters
    TypeValues = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)

    # Custom or Random len
    if LenP == 0: LenP = random.randint(8, 16)
    elif LenP < 4: raise ValueError("Your password is totally unsafe!")

    # Making the list
    uPass = [random.choice(TypeValues[i % 4]) for i in range(LenP)] 
    random.shuffle


# Suffle will move characters around in place and return none

# To solve that problem we can use Cyclic algorithm
# Cyclic algorithms get a number and return the corresponding in a specific range of numbers
# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

# To check if a number is prime or not, we have to check all the numbers before that
# Also, we exclude 1 for more explicitly because it is common in all primes and composites

def PrimeNum(limit): 
    for num in range(1, limit):
        isPrime = True 
        for j in range(2, num): 
            if num % j == 0:
                isPrime = False
                break
        if isPrime: yield num

for prime in PrimeNum(int(input("Your Limit: "))): print(prime, end=", ")

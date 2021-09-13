# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

# Easier way
def fibo(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for item in fibo(int(input('enter a number: '))): print(item)

# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

def even_odd(num):
    for i in range(num + 1):
        if i == 0: continue
        if i % 2 == 0:
            yield "Even : " + str(i)
        else:
            yield "Odd  : " + str(i)


number = int(input('please enter a number: '))
result = even_odd(number)
for item in result:
    print(item)

def reverser(stri):
    li = stri.split(' ')
    return ' '.join(li[::-1])

print(reverser(input("Enter a string: ")))

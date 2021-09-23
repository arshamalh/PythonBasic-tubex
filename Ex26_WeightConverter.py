# Weight Converter
weight = float(input("weight: "))

cond = input("kilogram(k) or pound(l)? ")
if cond.lower() == 'k':
    weight *= 2.2
    print(f"your weight is {weight} pounds")
elif cond.lower() == 'l':
    weight *= 0.4545
    print(f"your weight is {weight} kilograms")
else:
    print('something is wrong')

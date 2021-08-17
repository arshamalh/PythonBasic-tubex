# Add two integers without using the '+' operator
def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        print('data: ', data)
        a = a ^ b
        print('a: ', a)
        b = data << 1
        print('b: ', b)
    return a
print(add_without_plus_operator(2, 10))
print()
print(add_without_plus_operator(-20, 10))
print()
print(add_without_plus_operator(-10, -20))

"""
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.
"""


# last example solved on "https://www.w3resource.com/python-exercises/" => basics 2 => 30

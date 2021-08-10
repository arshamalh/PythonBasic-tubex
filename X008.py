# Test if circumference of two circles intersect or overlap
print("Input x1, y1, r1, x2, y2, r2:")
x1, y1, r1, x2, y2, r2 = [float(i) for i in input().split()]
d = pow(((x1-x2)**2 + (y1-y2)**2), 0.5)  # it's something like math.sqrt
if d < r1-r2:
    print("C2  is in C1")
elif d < r2-r1:
    print("C1  is in C2")
elif d > r1+r2:
    print("Circumference of C1  and C2  intersect")
else:
    print("C1 and C2  do not overlap")

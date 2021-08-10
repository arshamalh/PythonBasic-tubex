# Get the size of an object in bytes
import sys
str1 = "one"
str2 = "four"
str3 = "three"
print()
print(f"Memory size of '{str1}' = {sys.getsizeof(str1)} bytes")
print(f"Memory size of '{str2}' = {sys.getsizeof(str2)} bytes")
print(f"Memory size of '{str3}' = {sys.getsizeof(str3)} bytes")
print()

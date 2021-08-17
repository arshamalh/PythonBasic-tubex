# Check whether a file path is a file or a directory
import os
path = "abc.txt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)")
print()

# Get File Size
import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :", file_size, "Bytes")
print()

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

# Display a floating number in specified numbers
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()


# Determine the largest and smallest integers, longs, floats
import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize)


# Get the system time
# Note : The system time is important for debugging,
# network information, random number seeds, or something as simple as program performance.
import time
print()
print(time.ctime())
print()

# Get the name of the host on which the routine is running
import socket
host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()
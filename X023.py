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

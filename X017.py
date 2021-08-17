import os
import time
from datetime import datetime
list_of_files = os.listdir(os.getcwd())
list_of_files.sort(key=os.path.getctime)
list_of_times = [datetime.strptime(time.ctime(os.path.getctime(a)), "%a %b %d %H:%M:%S %Y") for a in list_of_files]
for name, time in zip(list_of_files, list_of_times):
    print(f'{name}: {time.strftime("%A %d %B %Y - %H:%M:%S")}')


# Concatenate N strings
list_of_colors = ['Red', 'White', 'Black']
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()

# Check whether lowercase letters exist in a string
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))

# Convert an integer to binary keep leading zeros
x = 12
print(format(x, '08b'))
print(format(x, '010b'))

# Convert decimal to hexadecimal
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))


# Get a list of locally installed Python modules
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
for m in installed_packages_list:
    print(m)
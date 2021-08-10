import os
import time
from datetime import datetime

list_of_files = os.listdir(os.getcwd())
list_of_files.sort(key=os.path.getctime)
list_of_times = [datetime.strptime(time.ctime(os.path.getctime(a)), "%a %b %d %H:%M:%S %Y") for a in list_of_files]
for name, time in zip(list_of_files, list_of_times):
    print(f'{name}: {time.strftime("%A %d %B %Y - %H:%M:%S")}')



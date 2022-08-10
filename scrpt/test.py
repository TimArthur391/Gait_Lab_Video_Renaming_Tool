#from db_connection import  connect_to_database
#connect_to_database('Arthurt', '2022-06-10', '11:27:30', 'old file name', 'new file name', 104.33)
from datetime import datetime
import os
import socket
now = datetime.now()
old_time = datetime(2022,6,10,13,20)
print(old_time)
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
time_diff = now - old_time
duration = time_diff.total_seconds()
print(socket.gethostbyname(socket.gethostname()))

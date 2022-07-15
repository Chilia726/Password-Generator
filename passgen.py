# Password generator

import random
import pyfiglet
import os
import time

os.system('cls')
time.sleep(0.5)
r = pyfiglet.figlet_format("PASSGEN")
print(r)
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "[]{}#()*;._"
ans = lower_case + upper_case + num + symbol

length = 9
password = "".join(random.sample(ans,length))
print("Generated password is:", password)
input("Press any enter to continue...")
print("Finished!")
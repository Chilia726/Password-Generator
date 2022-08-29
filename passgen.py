# Password generator

import random
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

command = os.system
delay = time.sleep
say = print

command('color d')
command('cls')
delay(0.5)
say(" ____   _    ____ ____   ____ _____ _   _  __     ______  ")
say("|  _ \ / \  / ___/ ___| / ___| ____| \ | | \ \   / /___ \ ")
say("| |_) / _ \ \___ \___ \| |  _|  _| |  \| |  \ \ / /  __) |")
say("|  __/ ___ \ ___) |__) | |_| | |___| |\  |   \ V /  / __/ ")
say("|_| /_/   \_\____/____/ \____|_____|_| \_|    \_/  |_____|\n\n\n")

say(Fore.LIGHTRED_EX + "[1] Generate a 9 character password")
say(Fore.LIGHTRED_EX + "[2] Generate a 15 character password")
say(Fore.LIGHTRED_EX + "[3] Bulk Generate 10 passwords in a text file")
say(Fore.LIGHTMAGENTA_EX + "[4] Exit the program")
def passgen():
    inp = input(Fore.CYAN + "Option: ")
    if inp == "1":
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        symbol = "[]{#}()*;._!@$%&"
        ans = lower_case + upper_case + num + symbol

        length = 9
        password = "".join(random.choices(ans,k=length))
        command('cls')
        print(Fore.LIGHTGREEN_EX + "Generated password is:", password)
        print(Fore.LIGHTGREEN_EX + "Made by floppa#4641")

        input(Fore.LIGHTCYAN_EX + "Press enter to continue...")
        print(Fore.LIGHTCYAN_EX + "Finished!")

    elif inp == "2":
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        symbol = "[]{#}()*;._!@$%&"
        ans = lower_case + upper_case + num + symbol

        length = 15
        password = "".join(random.choices(ans,k=length))
        command('cls')
        print(Fore.LIGHTGREEN_EX + "Generated password is:", password)
        print(Fore.LIGHTGREEN_EX + "Made by floppa#4641")

        input(Fore.LIGHTCYAN_EX + "Press enter to continue...")
        print(Fore.LIGHTCYAN_EX + "Finished!")

    elif inp == "3":
        command('cls')
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890[]{#}()*;._!@$%&"
        for i in range(10):
            first = ''.join((random.choice(chars) for i in range(13)))

            result = first


            output = open('passwords.txt', 'a')
            output.write(result + "\n")

    elif inp == "4":
        command('exit')
        command('exit')

    else:
        say("Error, Unknown command, Please try again.")
        return passgen()
passgen()
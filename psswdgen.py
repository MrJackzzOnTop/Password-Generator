import secrets, string
import colorama
from colorama import Fore, Back, Style
colorama.init()
import sys,time
import os

os.system('title Password Generator By 4ZHelter')

if sys.platform == 'win32':
   os.system("cls")

if sys.platform == 'linux':
    os.system("clear")

logo = ("""
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                          
""")

credits = ("""                             _________________________________________
                            |                                         |
                            | Coded by: https://github.com/44ZHelter  |
                            |_________________________________________| 
""")

print(Fore.BLUE + logo)
print(Fore.YELLOW + credits)

length = input(Fore.RED + "[?] Choose your password length: ")

passwords = input(Fore.MAGENTA + "[?] How many passwords you want to generate?: ")

lower_case = "abcdefghijklmnopqrtsuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symbol = "!$%&/()=@#€[]{}+-*_"


ans = lower_case + upper_case + num + symbol



for i in range(int(passwords)):
    password = ''.join(secrets.choice(ans) for i in range(int(length)))
    print(Fore.GREEN + "[!] Your Generated Password is: " + password)

name = "[*] Thanks for using this Password Generator, now you can close this window."

for l in name:
    sys.stdout.flush()
    print( Fore.LIGHTCYAN_EX + l,end="")
    time.sleep(0.1)

input()

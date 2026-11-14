import secrets, string
import sys,time
import os

os.system('title Password Generator By MrJackzzOnTop')

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

credits = ("""
                             ____________________________________________
                            |                                            |
                            | Coded by: https://github.com/MrJackzzOnTop |
                            |____________________________________________|
""")

RED = "\033[38;2;255;0;0m"
GREEN = "\033[38;2;0;255;0m"
BLUE = "\033[38;2;0;0;255m"
YELLOW = "\033[38;2;255;255;0m"
CYAN    = "\033[36m"


print(BLUE + logo)
print(RED + credits)

length = input(YELLOW + "[?] Choose your password length: ")

passwords = input(YELLOW + "[?] How many passwords you want to generate?: ")

lower_case = "abcdefghijklmnopqrtsuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symbol = "!$%&/()=@#€[]{}+-*_"

include_lower_case = input(GREEN + "[?] Include lower case characters? (Y/n): ").upper()
include_upper_case = input(GREEN + "[?] Include upper case characters? (Y/n): ").upper()
include_num = input(GREEN + "[?] Include numbers? (Y/n): ").upper()
include_symbol = input(GREEN + "[?] Include symbols? (Y/n): ").upper()

ans = ""

if include_lower_case == "Y":
    ans += lower_case

if include_upper_case == "Y":
    ans += upper_case

if include_num == "Y":
    ans += num

if include_symbol == "Y":
    ans += symbol

if not ans:
    print(RED + "[!] ERROR: You must select at least one character type.")

for i in range(int(passwords)):
    password = ''.join(secrets.choice(ans) for i in range(int(length)))
    print(YELLOW + "[+] Your Generated Password is: " + password)

name = "[*] Thanks for using this Password Generator, now you can close this window."

for l in name:
    sys.stdout.flush()
    print(CYAN + l,end="")
    time.sleep(0.1)

input()

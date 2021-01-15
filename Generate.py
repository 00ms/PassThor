import random
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'            #Colors
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.HEADER}""""
  ____              _____ _   _  ___  ____  
 |  _ \ __ _ ___ __|_   _| | | |/ _ \|  _ \ 
 | |_) / _` / __/ __|| | | |_| | | | | |_) |
 |  __/ (_| \__ \__ \| | |  _  | |_| |  _ < 
 |_|   \__,_|___/___/|_| |_| |_|\___/|_| \_\

""")

password_length = 9    # you can change this to whatever value you like
possible_characters = "abcdefghijklmnopqrstuvwxyz12345613123sda*_x7890"

random_character_list = [random.choice(possible_characters) for i in range(password_length)]
password_s = "".join(random_character_list)

prompt1 = input(f"{bcolors.OKCYAN}" + 'Do you want to Generate strong password type "yes" to generate \n : ').lower()

if prompt1 == 'yes':
    time.sleep(0.5)
    print(f"{bcolors.OKBLUE}" + "your password is " + password_s)
elif prompt1 == 'no':
    print('Oopsies')
else:
    print(f"{bcolors.WARNING}" +'wut?')  # response to an input that is not defined
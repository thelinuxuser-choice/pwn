##########thelinuxuxer-choice#################
#############subodha prabash ##########
###########pwn checker passwords######

# arguments
import sys
if len(sys.argv) == 1:
	print(f'Usage: "python3 pwn.py <PASSWORD>"\n(Use "-h" option for more info)')
	sys.exit()
if '-h' in sys.argv or '--help' in sys.argv:
	print('''
Example usage: python3 pwn.py 1234 
-h                     To show this message''')
	sys.exit()

####loading section
#starting function

# importing the necessary packages 
import time 
import sys 
import os 
  
# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = "loading pwn tool..."
    ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of 
    # the duration of animation 
    counttime = 0        
      
    # pointer for travelling the loading string 
    i = 0                     
  
    while (counttime != 40): 
          
        # used to change the animation speed 
        # smaller the value, faster will be the animation 
        time.sleep(0.075)  
                              
        # converting the string to list 
        # as string is immutable 
        load_str_list = list(load_str)  
          
        # x->obtaining the ASCII code 
        x = ord(load_str_list[i]) 
          
        # y->for storing altered ASCII code 
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered 
        # switch uppercase to lowercase and vice-versa  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        # for storing the resultant string 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        # displaying the resultant string 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        # Assigning loading string 
        # to the resultant string 
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 
#####end loding######
############banner

banner = r'''
              />           
 ()          //------------------------------------------------------------------(
(*)OXOXOXOXO(*> pwn tool -coded by thelinuxuser-choice | password pawn checker    \
 ()          \\-------------------------------------------------------------------)
              \>            ▬▬ι═══════ﺤ|version: 1.0 ﺤ═══════ι▬▬ﺤ
                               ▬▬ι═══════ﺤ|status:checked and working ﺤ═══════ι▬▬ﺤ
                                  ▬▬ι═══════ﺤ|language:python3 ﺤ═══════ι▬▬ﺤ                            
'''
#colours
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))  
red = "\033[91m {}\033[00m"
prYellow(banner)




#interface ui

from time import sleep
import sys

line_1 = red+"pwn checker tool by thelinuxuser-choice "
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

prCyan("\nchecking the password!...")

# progress
import sys
import time


def updt(total, progress):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 10
for run_num in range(runs):
    time.sleep(.1)
    updt(runs, run_num + 1)


#####end######of progress######
prGreen("\n+++++++++++++++++++++++++++++++++++++++++++++++")


###################code

import requests
import hashlib
import sys


def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)
  


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
             print('\x1b[6;30;42m' + f'\n{password} was found {count} times in a data breach... \nyou should probably change your password!' + '\x1b[0m')
             prGreen("\n+++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            print('\x1b[6;30;42m' + f'\n{password} was NOT found in data breaches. \nCarry on!' + '\x1b[0m')           
            prGreen("\n+++++++++++++++++++++++++++++++++++++++++++++++")
    prRed("now you can enjoy your cofee!!")

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

##############end of code
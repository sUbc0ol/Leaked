import os
import json
import requests
from platform import system

def clear():
    if system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def back():
    print()
    back = input('\033[92mDo you want to contunue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        hashs()
    elif back[0].upper() == 'N':
        print('\033[93mRemember https://GitHackTools.blogspot.com')
        exit
    else:
        print('\033[92m?')
        exit

def banner():
    print("""\033[93m
 ___       _______   ________  ___  __    _______   ________  ________      
|\  \     |\  ___ \ |\   __  \|\  \|\  \ |\  ___ \ |\   ___ \|\_____  \     
\ \  \    \ \   __/|\ \  \|\  \ \  \/  /|\ \   __/|\ \  \_|\ \|____|\  \    
 \ \  \    \ \  \_|/_\ \   __  \ \   ___  \ \  \_|/_\ \  \ \\ \    \ \__\   
  \ \  \____\ \  \_|\ \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \_\\ \    \|__|   
   \ \_______\ \_______\ \__\ \__\ \__\\ \__\ \_______\ \_______\       ___ 
    \|_______|\|_______|\|__|\|__|\|__| \|__|\|_______|\|_______|      |\__\\
                                                                        \|__| 1.1
     A Checking tool for Hash codes and Passwords leaked""")
    print()

def hashs():
    try:
        print("""\033[96mWhat do you want to check?
    1, Password Leaked      3, About Author     
    2, Hash Leaked          4, No Check Anything! (Exit)""")
        print()

        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            print()
            nocode = input('Enter or paste a password you want to check: ')
            cipher = requests.get('https://lea.kz/api/password/'+nocode)
            js = json.loads(cipher.text)
            print("""\033[93mIT LEAKED!!! The Hash codes of the Password is:

MD5: """+js['md5']+"""
SHA1: """+js['sha1']+"""
SHA224: """+js['sha224']+"""
SHA256: """+js['sha256']+"""
SHA384: """+js['sha384']+"""
SHA512: """+js['sha512']+"""""")
            back()

        elif choice == '2':
            print()
            code = input('Enter or paste a hash code you want to check: ')
            decipher = requests.get('https://lea.kz/api/hash/'+code)
            js = json.loads(decipher.text)
            print('\033[93mTHAT HASH CODE IS LEAKED! It means: '+js['password'])
            back()

        elif choice == '3':
            print("""\033[93mLeaked? 1.1 - A Checking tool for Hash codes and Passwords leaked

    AUTHOR: https://GitHackTools.blogspot.com
            https://twitter.com/SecureGF
            https://fb.com/TVT618
            https://plus.google.com/+TVT618""")
            back()

        elif choice == '4':
            print('\033[93mRemember https://GitHackTools.blogspot.com')
            exit

        else:
            print('?')
            print()
            hashs()

    except KeyboardInterrupt:
        print()
        exit
    except requests.exceptions.ConnectionError:
        print('\033[91mYour Internet Offline!!!')
        exit
    except json.decoder.JSONDecodeError:
        print('\033[93mCongratulations! It does not leaked!!!')
        print()
        hashs()

clear()
banner()
hashs()
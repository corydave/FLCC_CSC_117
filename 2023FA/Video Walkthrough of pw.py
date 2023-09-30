# FILE NAME - password.py

# NAME - Dave Ghidiu
# DATE - September 30, 2023
# DESCRIPTION - This program will ask the user for a number to seed the RNG and then
#               generate a random password

import random
import string

def main():
    generatePassword()

def generatePassword():

    seed = int(input('Enter a seed for the random number generation: '))
    random.seed(seed)

    print()

    special_characters = '!@#$&(),-_'

    password = ''

    # password = password + random.choice(special_characters)
    password += random.choice(special_characters)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)    
    password += random.choice(string.digits)    
    password += random.choice(special_characters)

    print('Your random password is: ')
    print(password)
    
    




main()

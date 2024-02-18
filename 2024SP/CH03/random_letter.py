# SOLUTION for `random_letter.py`

import random
import string

def main():
    random_letter_generator()

def random_letter_generator():
    print('-----------------------')
    print('RANDOM LETTER GENERATOR')
    print('-----------------------')

    print()

    seed_from_user = int(input('Enter a seed for the random number generator: '))

    random.seed(seed_from_user)

    random_letter = random.choice(string.ascii_lowercase)

    print(f'The random letter is: {random_letter}')


main()
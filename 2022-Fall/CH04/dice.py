import random

def roll_die():
    die = random.randrange(1, 7)
    return die

def roll_die_sided(num_sides):
    '''
    A random die roll inclusive of 1 and inclusive of the argument you give it.
    EX: roll_die_sided(10) will give a random number 1-10
    '''

    die = random.randrange(1, num_sides + 1)
    return die

def roll_two_dice():
    die01 = roll_die()
    die02 = roll_die()
    
    dice_tuple = (die01, die02)
    # print('DEBUG:',dice_tuple)
    return dice_tuple

def roll_two_dice_sided(num_sides):
    die01 = roll_die_sided(num_sides)
    die02 = roll_die_sided(num_sides)

    dice_tuple = (die01, die02)

    return dice_tuple
    

# roll_two_dice_sided(20)
# roll_two_dice()
# roll_die_sided(2)
# roll_die()


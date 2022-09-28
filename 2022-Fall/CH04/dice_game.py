import dice
import util

def main():
    util.cls()
    dice_roller()

def dice_roller():
    die01 = dice.roll_die()
    die02 = dice.roll_die()

    # print("DEBUG:", die01, die02)

    total = die01 + die02

    print("The value of the two dice is", total)

    num_sides = int(input('How many sides? '))
    die03 = dice.roll_die_sided(num_sides)
    print('The value of the dice with', num_sides, 'sides is', die03)

    dice_tuple = dice.roll_two_dice()

    die04 = dice_tuple[0]
    die05 = dice_tuple[1]

    num_sides = int(input('How many sides? '))
    dice_tuple = dice.roll_two_dice_sided(num_sides)
    
    die06 = dice_tuple[0]
    die07 = dice_tuple[1]

    print('You rolled a', die06, 'and a', die07,'.')
    
main()

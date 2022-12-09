# ALPHA - not fault-tolerant

# TODO
#   - Include instructions in welcome()

player_1 = ''
player_2 = ''

# [Pennies, Nickels, Dimes, Quarters]
p1_coins = [1, 1, 1, 1]
p2_coins = [4, 3, 2, 1]
common_coins = [0, 0, 0, 0]


def main():
    welcome()
    get_player_names()

    play_game()

    # show_coins(player_1, p1_coins)
    # show_coins(player_2, p2_coins)
    # show_coins('Common', common_coins)

def welcome():
    print('Welcome to Pennywise!')
    print('RULES COMING...');

def get_player_names():

    global player_1
    global player_2

    player_1 = 'dave'
    player_2 = 'john'

    # player_1 = input('Enter the name for player 1: ')
    # player_2 = input('Enter the name for player 2: ')


    print('Hello,', player_1, 'and', player_2,' - May the odds be forever in your favor.\n')

def show_coins(name, coins):
    '''
    name is a String
    coins is a list of coins
    '''
    print(name, 'has', coins[0], 'pennies,', coins[1], 'nickels,', coins[2], 'dimes, and', coins[3], 'quarters.')


def check_status():
    print('\n==========================\n')
    print(player_1, p1_coins)
    print(player_2, p2_coins)
    print('Common:', common_coins)
    print('\n==========================\n')


def play_game():
    play_until_winner()


def play_until_winner():

    while True:

        move(player_1, p1_coins, common_coins)
        if check_for_loser(player_1, p1_coins) == True:
            print('GAME OVER!', player_1, 'loses!')
            return


        move(player_2, p2_coins, common_coins)
        if check_for_loser(player_2, p2_coins) == True:
            print('GAME OVER!', player_2, 'loses!')
            return

def move(name, coins, common):

    show_coins(name, coins)
    show_coins("Common", common_coins)
    coin_to_play = input('\nWhich coin would you like to play (p/n/d/q)? ')

    value = 0

    if coin_to_play.lower() == 'p':
        if coins[0] >= 1:
            coins[0] = coins[0] - 1
            common[0] = common[0] + 1
            value = 0
        else:
            print('ERROR - You don\'t have any more pennies')
    elif coin_to_play.lower() == 'n':
        if coins[1] >= 1:
            coins[1] = coins[1] - 1
            common[1] = common[1] + 1
            value = 4
        else:
            print('ERROR - You don\'t have any more nickels')
    elif coin_to_play.lower() == 'd':
        if coins[2] >= 1:
            coins[2] = coins[2] - 1
            common[2] = common[2] + 1
            value = 9
        else:
            print('ERROR - You don\'t have any more dimes')
    elif coin_to_play.lower() == 'q':
        if coins[3] >= 1:
            coins[3] = coins[3] - 1
            common[3] = common[3] + 1
            value = 24
        else:
            print('ERROR - You don\'t have any more quarters')            
    else:
        print('ERROR - Not a valid choice')

    while value > 0:
        show_coins('COMMON:', common_coins)
        coin_to_take = input('Which coin would you like to take (p/n/d/q or "none")? ')

        if coin_to_take.lower() == 'p' and value >= 1 and common[0] >= 1:
            coins[0] = coins[0] + 1
            common[0] = common[0] - 1
            value = value-1
        elif coin_to_take.lower() == 'n' and value >= 5 and common[2] >= 1:
            coins[1] = coins[1] + 1
            common[1] = common[1] - 1
            value = value-1
        elif coin_to_take.lower() == 'd' and value >= 10 and common[2] >= 1:
            coins[2] = coins[2] + 1
            common[2] = common[2] - 1
            value = value-1
        elif coin_to_take.lower() == 'q' and value >= 25 and common[3] >= 1:
            coins[3] = coins[3] + 1
            common[3] = common[3] - 1
            value = value-1
        elif coin_to_take.lower() == 'none':
            break;
        else:
            print('ERROR - Not a valid option')



    check_status()

def check_for_loser(name, coins):
    for num_of_coins in coins:
        if num_of_coins > 0:
            return False
    
    #[ 0 0 0 0 ]

    return True

main()

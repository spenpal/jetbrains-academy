# IMPORTS #
from random import randint


# FUNCTIONS #
def error_pencils_taken(pencils_taken, pencils_left):
    if not pencils_taken.isnumeric() or int(pencils_taken) not in [1, 2, 3]:
        print("Possible values: '1', '2' or '3'")
        return True
    elif int(pencils_taken) > pencils_left:
        print('Too many pencils were taken')
        return True
        
    return False


def error_pencils_left(pencils_left):
    if not pencils_left.isnumeric():
        print('The number of pencils should be numeric')
        return True
    elif int(pencils_left) <= 0:
        print('The number of pencils should be positive')
        return True
        
    return False


# MAIN #
players = ('Jack', 'Jill')

# Error checking for {pencils_left} using walrus operator
while error_pencils_left(pencils_left := input('How many pencils would you like to use:\n')): continue
pencils_left = int(pencils_left)

# Error checking for {current_player} using walrus operator
while (first_player := input(f'Who will be the first ({", ".join(players)}):\n')) not in players:
    print(f'Choose between {" and ".join(players)}')
player_idx = players.index(first_player)

# GAME STARTS #
while pencils_left > 0:
    print('|' * pencils_left)
    print(f'{players[player_idx]} turn!')
    
    if player_idx == 0:
        # Player's Turn
        # Error checking for {pencils_taken} using walrus operator
        while error_pencils_taken(pencils_taken := input(), pencils_left): continue
        pencils_taken = int(pencils_taken)
    else:
        # Bot's Turn
        winning_position = (pencils_left - 1) % 4 != 0
        pencils_taken = (pencils_left - 1) % 4 if winning_position else randint(1, min(3, pencils_left))
        print(pencils_taken)
            
    pencils_left -= pencils_taken
    player_idx = not player_idx
        
print(f'{players[player_idx]} won!')
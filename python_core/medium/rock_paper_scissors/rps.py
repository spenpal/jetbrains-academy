import random


def outcome(user, computer, rating):
    if computer in rps_counter[user]:
        print(f'Sorry, but the computer chose {computer}')
    elif user in rps_counter[computer]:
        print(f'Well done. The computer chose {computer} and failed')
        rating += 100
    else:
        print(f'There is a draw ({computer})')
        rating += 50

    return rating


# MAIN #
moves = ['rock', 'paper', 'scissors']
rps_counter = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

# Name
name = input('Enter your name: ')
print('Hello,', name)

# Get user rating
with open('rating.txt') as f:
    scores = {}
    for line in f:
        name, score = line.split()
        scores[name] = score
    rating = int(scores.get(name, '0'))

# User-defined moves
user_moves = input().strip()
if user_moves:
    moves = user_moves.split(',')
    for i, move in enumerate(moves):
        other_moves = moves[i + 1:] + moves[:i]
        half = len(other_moves) // 2
        rps_counter[move] = other_moves[:half]

valid_inputs = moves + ['!exit', '!rating']
print("Okay, let's start")

# Start game
while True:
    user = input()
    while user not in valid_inputs:
        print('Invalid input')
        user = input()

    if user == '!exit': break
    if user == '!rating':
        print('Your rating:', rating)
        continue

    computer = random.choice(moves)
    rating = outcome(user, computer, rating)

print('Bye!')

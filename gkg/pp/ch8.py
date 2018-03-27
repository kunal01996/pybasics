# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the
# players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

import random

options = ['scissors', 'paper', 'rock']

while True:
    val = input('Enter choice: ')
    internals = options[random.randint(0, 2)]
    print(random.randint(0, 2))
    if (val == 'rock' and internals == 'scissors') or (val == 'scissors' and internals == 'paper') or (val == 'paper' and internals == 'rock'):
        print('You won!')
        break
    else:
        print('Ooh! you lost!')
        choice = input('Enter choice, Y to continue & N to leave')
        if choice == 'Y':
            continue
        elif choice == 'N':
            break
        else:
            break

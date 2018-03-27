# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random as r

rand_num = r.randint(0, 10)

while True:
    choice = input('enter a number: ')
    if choice != 'exit' and int(choice) == rand_num:
        print('Guessed it right!')
        break
    elif choice != 'exit' and int(choice) < rand_num:
        print('Guessed it too low!')
        continue
    elif choice != 'exit' and int(choice) > rand_num:
        print('Guessed it too high!')
        continue
    elif choice == 'exit':
        break


# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...

import random as rd


# print(randomNumberInList)
# print(userNumberInList)

cows = 0
bulls = 0

while cows != 4:
    randomNumber = rd.randint(1000, 9999)

    userNumber = input('Enter a 4 digit number: ')

    randomNumberInList = list(str(randomNumber))
    userNumberInList = list(str(userNumber))

    print(randomNumberInList)
    print(userNumberInList)

    for i in range(len(randomNumberInList)):
        if randomNumberInList[i] == userNumberInList[i]:
            cows += 1
        else:
            bulls += 1

    print('Cows {} and bulls {}.'.format(cows, bulls))

    cows = 0
    bulls = 0


# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity
# to practice using functions, described below.


def is_prime(number):
    count = 1

    if number == 1:
        print('Unique number!')
        return

    for i in range(1, number+1):
        if number % i == 0:
            count += count

    if count <= 2:
        print('Is prime!')
    else:
        print('Not prime!')


is_prime(int(input('Please enter a number: ')))


# Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not the given number
#  is inside the list and returns (then prints) an appropriate boolean.


import random

randList = [random.randint(10, 99) for i in range(11)]
randList.sort()
print(randList)


def binary_search(list_):
    """
    Binary Search
    :param list:
    :return:
    """

    userInput = int(input('Please enter a number <100: '))

    while True:
        length = len(list_)
        print(length//2)
        if length // 2 == 0:
            mid = list_[(length // 2) + 1]
        else:
            mid = list_[length // 2]

        if mid == userInput:
            print('Element found at position {}'.format((length // 2)))
            return True

        elif mid < userInput:
            list_ = list_[((length // 2) + 1):]

        elif mid > userInput:
            list_ = list_[0:((length // 2) + 1)]
        print(list_)

        print(mid)


binary_search(randList)


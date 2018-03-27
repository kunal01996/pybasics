# Write a program (function!) that takes a list and returns a new list that contains all the
# elements of the first list minus all the duplicates.
#
# Extras:
#
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def minus_duplicates(list):
    """
    List - duplicates
    :param list:
    :return:
    """
    min_list = []

    for i in list:
        if i in min_list:
            continue
        else:
            min_list.append(i)

    return min_list

          
print(minus_duplicates([1, 3, 8, 3, 3, 3, 4, 5, 2, 1, 76, 7, 89]))

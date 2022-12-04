#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    isDivisible = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            isDivisible.append(True)
        else:
            isDivisible.append(False)

    return (isDivisible)

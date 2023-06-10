#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    x = my_list.copy()
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            x[a] = 1
        else:
            x[a] = 0
    return x

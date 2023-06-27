#!/usr/bin/python3
def safe_print_list_integers(my_list=[], y=0):
    i = 0
    for j in range(0, y):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except(ValueError, TypeError):
            continue
    print("")
    return (i)

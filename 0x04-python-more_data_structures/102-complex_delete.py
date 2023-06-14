#!/usr/bin/python3
def complex_delete(my_dict, value):
    y = []
    for x in my_dict:
        if my_dict[x] == value:
            y.append(x)
    for x in y:
        del my_dict[x]
    return my_dict

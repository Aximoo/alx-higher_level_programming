#!/usr/bin/python3
def complex_delete(my_dict, value):
    keys_to_del = []
    for i in my_dict:
        if my_dict[i] == value:
            keys_to_del.append(key)
    for i in keys_to_del:
        del my_dict[i]
    return my_dict

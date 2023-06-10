#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    hex = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        hex[idx] = element
        return hex

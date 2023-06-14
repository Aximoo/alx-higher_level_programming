#!/usr/bin/python3
def search_replace(my_list, search, replace):
    j = []
    for i in my_list:
        if i == search:
            j.append(replace)
        else:
            j.append(i)
    return j

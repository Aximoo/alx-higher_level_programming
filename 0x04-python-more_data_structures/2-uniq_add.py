#!/usr/bin/python3
def uniq_add(my_list=[]):
    q = 0
    for x in set(my_list):
        q += x
    return q

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = ()
    i = tuple_a + (0, 0)
    j = tuple_b + (0, 0)
    x = i[0] + j[0], i[1] + j[1]
    return x

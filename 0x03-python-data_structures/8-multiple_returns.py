#!/usr/bin/python3

def multiple_returns(sentence):
    y = len(sentence)
    if y == 0:
        z = (0, None)
        return z
    else:
        m = (y, sentence[0:1])
        return m

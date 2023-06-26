#!/usr/bin/python3
def magic_calculation(a, b):
    y = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            y += a ** b / i
        except:
            y = b + a
            break
        return y

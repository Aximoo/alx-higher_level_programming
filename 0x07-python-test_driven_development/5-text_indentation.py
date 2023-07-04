#!/usr/bin/python3
"""
Thiss is the "5-test_indentation" module.
The 5-text_indentations module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for y in text:
        if flag == 0:
            if y == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if y == '?' or y == '.' or y == ':':
                print(y)
                print()
                flag = 0
            else:
                print(y, end="")

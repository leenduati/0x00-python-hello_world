#!/usr/bin/bash


def uppercase(str):
    sol = ''
    res = 0
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            res = ord(str[i]) - 32
            sol += chr(res)
        else:
            sol += str[i]
    print(sol)

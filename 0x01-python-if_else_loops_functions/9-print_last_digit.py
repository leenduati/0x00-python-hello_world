#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        number = number * -1
    sol = number % 10
    print(sol, end="")
    return sol

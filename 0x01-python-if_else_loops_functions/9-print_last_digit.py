#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        mod = number % 10
        print(mod, end="")
        return mod
    elif number < 0:
        mod = -number % 10
        print(mod, end="")
        return mod
    else:
        print(number, end="")
        return number

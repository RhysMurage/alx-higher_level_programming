#!/usr/bin/python3
def safe_print_division(a, b):
    val = 0
    try:
        value = a/b
    except ZeroDivisionError:
        value = None
    finally:
        print("Inside result: {}".format(val))
        return (val)

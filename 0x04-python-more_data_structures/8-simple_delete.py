#!/usr/bin/python3
def simple_delete(a_dictionary, keys=""):
    if keys in list(a_dictionary.keys()):
        a_dictionary.pop(keys)
    return a_dictionary

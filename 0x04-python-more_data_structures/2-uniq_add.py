#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = 0
    new_list = []
    for initial in my_list:
        if initial not in new_list:
            new_list.append(initial)
    for x in new_list:
        y += x
    return y

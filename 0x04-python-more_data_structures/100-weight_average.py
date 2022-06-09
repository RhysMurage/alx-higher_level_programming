#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        x = 0
        y = 0
        for tup in my_list:
           x += tup[1]
           y += (tup[0] * tup[1])/x
        return(y)
    else:
        return(0)

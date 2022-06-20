#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        length1 = 0
        str1 = ''.join(str(i) for i in my_list[:x])
        print(str1)
        for i in my_list[:x]:
            length1 += 1
        return length1
    except IndexError:
        length2 = 0
        print(str1)
        for i in my_list:
            length2 += 1
        return length2

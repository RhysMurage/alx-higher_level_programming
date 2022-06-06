#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    results = []
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) == 0:
        return tuple_a
    for x, y in zip(tuple_a, tuple_b):
        zipped = x+y
        results.append(zipped)
    return tuple(results)

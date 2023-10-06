#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    if len(tuple_a) < 0:
        tuple_a = 0, 0
    elif len(tuple_b) < 0:
        tuple_b = 0, 0
    elif len(tuple_a) > 2:
        y = list(tuple_a)
        y.remove[2:]
        tuple_a = tuple(y)
    elif len(tuple_b) > 2:
        y = list(tuple_b)
        y.remove[2:]
        tuple_b = tuple(y)
    else:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

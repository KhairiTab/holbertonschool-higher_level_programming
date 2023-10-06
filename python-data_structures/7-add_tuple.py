#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    if len(tuple_a) <0:
        return 0
    elif len(tuple_a) >2:
        y = list(tuple_a)
        y.remove[2:]
        tuple_a = tuple(y)
    elif len(tuple_b) >2:
        y = list(tuple_b)
        y.remove[2:]
        tuple_b = tuple(y)
    else:
        for i in range(len(list_a)):
            list_a[i] += tuple_b[i]
    tuple_a = tuple(list_a)
    return(tuple_a)

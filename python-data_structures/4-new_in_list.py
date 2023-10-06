#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_b = []
    if idx < 0:
        return my_list
    elif idx >= (len(my_list)-1):
        return my_list
    
    list_b = [x for x in my_list]
    list_b[idx] = element
    return (list_b)

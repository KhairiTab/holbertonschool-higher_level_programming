#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_b = []
    if idx < 0:
        return my_list
    elif idx >= (len(my_list)-1):
        return my_list
    else:
        for i in range(len(my_list)-1):
            list_b[i] = my_list[i]
    list_b[idx] = element

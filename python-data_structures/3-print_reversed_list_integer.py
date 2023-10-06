#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse=True) 
    for i in range(len(my_list)):
        print("{}".format(int(my_list[i])))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if not my_list:
        pass

    new_list = my_list
    new_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(new_list[i]))

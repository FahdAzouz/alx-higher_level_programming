#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    r_num = 0
    for i in range(x):
        if my_list[i] is int:
            try:
                print("{:d}".format(my_list[i]), end="")
                r_num += 1
            except IndexError:
                break
    print()
    return r_num

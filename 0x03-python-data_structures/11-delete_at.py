#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if not my_list:
        pass
    else:
        if idx >= 0 and idx < len(my_list):
            my_list[idx] = []
            return my_list
        else:
            return my_list
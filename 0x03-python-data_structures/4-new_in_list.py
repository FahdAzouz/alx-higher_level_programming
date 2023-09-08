#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    mylist = my_list.copy()
    if idx >= 0 and idx < len(mylist):
        mylist[idx] = element
        return mylist
    else:
        return mylist

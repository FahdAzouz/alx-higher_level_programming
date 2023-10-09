#!/usr/bin/python3

"""
1-my_list module
"""


class MyList(list):
    """
    MyList child of list
    """
    def print_sorted(self):
        """
        print_sorted - prints the list sorted
        """
        print(sorted(self))

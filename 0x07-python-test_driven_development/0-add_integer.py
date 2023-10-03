#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """
    Function That Adds two integers

    Args:
        b: second integer
        a: first integer

    Returns:
        addition of two integers
    """
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    else:
        new_a = int(a)
        new_b = int(b)
        return new_a + new_b

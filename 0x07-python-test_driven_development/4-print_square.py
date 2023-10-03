#!/usr/bin/python3
"""
    4-print_square Module
"""

def print_square(size):
    """
        Prints a square with characters '#'

        Args:
            size: size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        for k in range(size):
            print("#", end='')
        print()

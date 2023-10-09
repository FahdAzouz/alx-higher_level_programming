#!/usr/bin/python3

"""
lookup - returns the list of available attributes and methods of an object
@obj: Object
Return: list object
"""

def lookup(obj):
    """ return list of obj"""
    return dir(obj)

#!/usr/bin/python3
"""
base.py
"""
import json
import os
import csv
import turtle


class Base:
    """
    Base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - initialization
        Args:
            id: object id
        """
        if id not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects

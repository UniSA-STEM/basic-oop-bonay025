"""
File: Hacker.py
Description: This module holds the Hacker class which represents a hacker object.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    """This class represents a Hacker object."""
    def __init__(self, name, inventory):
        self.__name = name
        self.__inventory = []
        self.__trace_level = 0
        self.__exposed = False

    def __str__(self):
        return (f"Name: {self.__name} \n"
                f"Rig: \n"
                f"Trace Level: {self.__trace_level} \n"
                f"Inventory: {self.__inventory}")
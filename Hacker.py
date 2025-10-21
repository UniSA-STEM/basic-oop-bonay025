"""
File: Hacker.py
Description: This module holds the Hacker class which represents a hacker object.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from os import remove

from Asset import Asset
from Rig import Rig

class Hacker:
    """This class represents a Hacker object."""
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset.get_name(Asset("CryptoToken", "Used to acquire or repair rigs", False))]
        self.__trace_level = 0
        self.__exposed = False
        self.__rig = None

    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_trace_level(self):
        return self.__trace_level

    def get_exposed(self):
        return self.__exposed

    def get_rig(self):
        return self.__rig

    def acquire_rig(self, name):
        self.__rig = Rig(name)
        self.__inventory.remove("CryptoToken")

    def __str__(self):
        return (f"Name: {self.__name} \n"
                f"Rig: {Rig.get_name(self.__rig)}\n"
                f"Trace Level: {self.__trace_level} \n"
                f"Inventory: {self.__inventory}")


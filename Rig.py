"""
File: Rig.py
Description: This module holds the Rig class which represents a Rig (computer) object.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    """This class represents a Rig(computer) object."""
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__upgrade_level = 0

    def get_name(self):
        return self.__name

    def get_damage_count(self):
        return self.__damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def get_storage(self):
        return self.__storage

    def get_upgrade_level(self):
        return self.__upgrade_level

    def __str__(self):
        return (f"{self.__name} \n"
                f"{self.__broken_state} \n"
                f"{self.__upgrade_level} \n"
                f"{self.__storage} \n")

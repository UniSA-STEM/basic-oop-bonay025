"""
File: Asset.py
Description: This module hold the Asset class which represents a digital asset.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        return self.__name

    def get_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"
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
        self.__inventory = [Asset.get_name(Asset("CryptoToken", "Used to acquire or repair rigs"))]
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

    def increase_trace_level(self):
        self.__trace_level += 1
        if self.__trace_level > 5:
            self.__exposed = True

    def launch_data_spike(self, rig):
        storage = self.__rig.get_storage()
        if "Data Spike" not in storage:
            print(f"You need a Data Spike in your Rig to launch data spike.")
        else:
            rig.take_hit()

    #def encrypt_asset(self, asset):

    def upgrade_rig(self):
        if self.__rig is None:
            print("You must first acquire a rig.")
        elif "Hardware Patch" not in self.__inventory:
            print("You must first acquire a Hardware Patch.")
        else:
            self.__inventory.remove("Hardware Patch")
            Rig.upgrade(self.__rig)

    def store_asset(self, asset):
        self.__inventory.remove(asset)
        Rig.release_asset(asset)

    def retrieve_asset(self, asset):
        self.__inventory.append(asset)
        Rig.store_asset(asset)


    def scan_inventory(self, name):
        for asset in self.__inventory:
            if asset == name:
                self.__inventory.remove(asset)
                print(asset)


    def __str__(self):
        return (f"Name: {self.__name} \n"
                f"Rig: {self.__rig}\n"
                f"Trace Level: {self.__trace_level} \n"
                f"Inventory: {self.__inventory}")



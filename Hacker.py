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
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.")]
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
        for asset in self.__inventory:
            if asset.get_name() == "CryptoToken":
                self.__inventory.remove(asset)

    def increase_trace_level(self):
        self.__trace_level += 1
        if self.__trace_level > 5:
            self.__exposed = True

    def launch_data_spike(self, rig):
        storage = []
        for asset in self.__rig.get_storage():
            storage.append(asset.get_name())
        print(storage)
        if 'Data Spike' not in storage:
            print(f"You need a Data Spike in your Rig to launch data spike.")
        #else:
            #rig.take_hit()

    def encrypt_asset(self, asset):
        if asset not in self.__inventory:
            print(f"You don't have a {asset.get_name()} to encrypt.")
        elif "Security Chip" not in self.__inventory:
            print(f"You need a Security Chip to encrypt.")
        else:
            asset.set_encrypted(True)

    def upgrade_rig(self):
        if self.__rig is None:
            print("You must first acquire a rig.")
        elif Asset.get_name() == "Hardware Patch" not in self.__inventory:
            print("You must first acquire a Hardware Patch.")
        else:
            self.__inventory.remove("Hardware Patch")
            Rig.upgrade(self.__rig)

    def store_asset(self, asset):
        self.__inventory.remove(asset)
        self.__rig.release_asset(asset)

    def retrieve_asset(self, asset):
        storage = self.__rig.get_storage()
        print(storage)
        if asset not in storage:
            print(f"You need a {asset} in your Rig to retrieve it.")
        else:
            self.__rig.store_asset(asset)


    def scan_inventory(self, name):
        for asset in self.__inventory:
            if asset.get_name() == name:
                self.__inventory.remove(asset)
                print(asset)


    def __str__(self):
        str_inventory = ""
        for asset in self.__inventory:
            str_inventory += asset.get_name() + "\n"
        return (f"Name: {self.__name} \n"
                f"Rig: {self.__rig}\n"
                f"Trace Level: {self.__trace_level} \n"
                f"Inventory: {str_inventory}")

hacker = Hacker("Hacker")
print(hacker)
hacker.acquire_rig("ben")
print(hacker)



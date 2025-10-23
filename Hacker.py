"""
File: Hacker.py
Description: This module holds the Hacker class which represents a hacker object.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""

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
        else:
            self.retrieve_asset(Asset("Data Spike", "Used in battles."))
            for item in self.__inventory:
                if item.get_name() == "Data Spike":
                    self.__inventory.remove(item)
            rig.take_hit()
            if rig.get_broken_state():
                rig_storage = []
                for item in rig.get_storage():
                    rig_storage.append(item)
                for asset in rig_storage:
                    if asset.get_encrypted() is False:
                        rig.store_asset(asset)
                        self.__inventory.append(asset)


    def encrypt_asset(self, asset):
        for item in self.__inventory:
            if item.get_name() == asset.get_name():
                if item.get_encrypted() is False:
                    item.set_encrypted(True)

    def upgrade_rig(self):
        if self.__rig is None:
            print("You must first acquire a rig.")
        else:
            for item in self.__inventory:
                if item.get_name() == "Hardware Patch":
                    self.__inventory.remove(item)
            Rig.upgrade(self.__rig)

    def repair_rig(self):
        if self.__rig is None:
            print("You must first acquire a rig.")
        else:
            for item in self.__inventory:
                if item.get_name() == "CryptoToken":
                    self.__inventory.remove(item)
            Rig.repair(self.__rig)

    def store_asset(self, asset):
        for item in self.__inventory:
            if item.get_name() == asset.get_name():
                self.__inventory.remove(item)
        self.__rig.release_asset(asset)
        self.increase_trace_level()

    def retrieve_asset(self, asset):
        self.__inventory.append(asset)
        self.__rig.store_asset(asset)
        self.increase_trace_level()

    def scan_inventory(self, name):
        for asset in self.__inventory:
            if asset.get_name() == name:
                self.__inventory.remove(asset)
                print(asset)


    def __str__(self):
        str_inventory = ""
        for asset in self.__inventory:
            str_inventory += f"{asset} \n"
        return (f"Name: {self.__name} \n"
                f"Rig: {self.__rig}\n"
                f"Trace Level: {self.__trace_level} \n"
                f"Inventory: {str_inventory} \n"
                f"")

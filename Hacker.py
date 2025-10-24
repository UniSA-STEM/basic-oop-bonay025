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

    def acquire_rig(self, rig):
        self.__rig = rig
        for asset in self.__inventory:
            if asset.get_name() == "CryptoToken":
                self.__inventory.remove(asset)
        print(f"You have acquired {self.__rig.get_name()}.\n")

    def increase_trace_level(self):
        self.__trace_level += 1
        if self.__trace_level > 5:
            self.__exposed = True

    def launch_data_spike(self, rig):
        if self.__rig is None:
            print(f"{self.__name} must acquire a rig first.")
        else:
            storage = []
            for asset in self.__rig.get_storage():
                storage.append(asset.get_name())
            if 'Data Spike' not in storage:
                print(f"You need a Data Spike in your Rig to launch data spike.\n")
            else:
                rig.take_hit()
                self.retrieve_asset(Asset("Data Spike", "Used in battles."))
                for item in self.__inventory:
                    if item.get_name() == "Data Spike":
                        self.__inventory.remove(item)
                self.increase_trace_level()

    def encrypt_asset(self, asset):
        for item in self.__inventory:
            if item.get_name() == asset.get_name():
                if item.get_encrypted() is False:
                    item.set_encrypted(True)
        for item in self.__rig.get_storage():
            if item.get_name() == asset.get_name():
                if item.get_encrypted() is False:
                    item.set_encrypted(True)

    def decrypt_asset(self, asset):
        for item in self.__inventory:
            if item.get_name() == asset.get_name():
                if item.get_encrypted() is False:
                    item.set_encrypted(True)
        for item in self.__rig.get_storage():
            if item.get_name() == asset.get_name():
                if item.get_encrypted() is False:
                    item.set_encrypted(True)

    def upgrade_rig(self):
        if self.__rig is None:
            print("You must first acquire a rig.\n")
        else:
            inventory = []
            for item in self.__inventory:
                inventory.append(item.get_name())
            if "Hardware Patch" not in inventory:
                print(f"You need a Hardware Patch to upgrade. \n")
            else:
                for item in self.__inventory:
                    if item.get_name() == "Hardware Patch":
                        self.__inventory.remove(item)
                Rig.upgrade(self.__rig)

    def repair_rig(self):
        if self.__rig is None:
            print("You must first acquire a rig.\n")
        else:
            for item in self.__inventory:
                if item.get_name() == "CryptoToken":
                    self.__inventory.remove(item)
            Rig.repair(self.__rig)

    def store_asset(self, asset):
        inventory = []
        for item in self.__inventory:
            inventory.append(item.get_name())
        if asset.get_name() not in inventory:
            print(f"You need a {asset.get_name()} "
                  f"in inventory to store it. \n")
        else:
            for item in self.__inventory:
                if item.get_name() == asset.get_name():
                    if item.get_encrypted() is False:
                        self.__inventory.remove(item)
                    else:
                        print(f"You need to decrypt the {asset.get_name()} to move it.\n")
            self.__rig.release_asset(asset)

    def retrieve_asset(self, asset):
        storage = []
        for item in self.__rig.get_storage():
            storage.append(item.get_name())
        name = asset.get_name()
        if name not in storage:
            print(f"You need a {asset.get_name()} in "
                  f"{self.__rig.get_name()} to retrieve it. \n")
        else:
            if item.get_encrypted() is False:
                self.__inventory.append(asset)
                self.__rig.store_asset(asset)
            else:
                print(f"You need to decrypt the {asset.get_name()} to move it.\n")

    def scan_inventory(self, asset):
        inventory = []
        for item in self.__inventory:
            inventory.append(item.get_name())
        if asset.get_name() not in inventory:
            print(f"You don't have {asset.get_name()} in your inventory. \n")
        else:
            for assets in self.__inventory:
                if asset.get_name() == assets.get_name():
                    self.__inventory.remove(assets)
                    print(asset)

    def __str__(self):
        str_inventory = ""
        for asset in self.__inventory:
            str_inventory += f"{asset} \n"
        str_rig = ""
        if self.__rig is None:
            str_rig = "None"
        else:
            str_rig = self.__rig.get_name()
        return (f"Name: {self.__name} \n"
                f"Rig: {str_rig}\n"
                f"Trace Level: {self.__trace_level} \n"
                f"---------- \n"
                f"Inventory: \n "
                f"{str_inventory} "
                f"---------- \n"
                f"")

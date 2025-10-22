"""
File: Rig.py
Description: This module holds the Rig class which represents a Rig (computer) object.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset

class Rig:
    """This class represents a Rig(computer) object."""
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__max_damage = 2
        self.__broken_state = False
        self.__storage = [Asset("Data Spike", "Used in battles."),
                          Asset("Data Spike", "Used in battles."),
                          Asset("Removable Drive", "Found in Rigs and used for extraction")]
        self.__storage_space = 4
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

    def repair(self):
        if "CryptoToken" not in self.__storage:
            print(f"You need a CryptoToken to repair the Rig.")
        else:
            if self.__broken_state:
                self.__broken_state = False
                self.__damage_counter = 0
            else:
                print(f"Rig is not broken. No repair needed.")

    def upgrade(self):
        self.__upgrade_level += 1
        self.__max_damage += 2
        self.__storage_space += 1

    def take_hit(self):
        self.__damage_counter += 1
        if self.__damage_counter == self.__max_damage:
            self.__broken_state = True

    def generate_asset(self):
        list_assets = [Asset("CryptoToken", "Used to acquire or repair rigs."),
                       Asset("Data Spike", "Used in battles."),
                       Asset("Removable Drive", "Found in Rigs and used for extraction."),
                       Asset("Security Chip", "Used to encrypt or decrypt assets."),
                       Asset("Hardware Patch", "Used to upgrade rigs.")]
        asset = random.choice(list_assets)
        self.__storage.append(Asset.get_name(asset))

    #def store_asset(self, asset):
        #self.__storage.remove(asset)

    #def release_asset(self, asset):
        #self.__storage.append(asset)

    def __str__(self):
        str_storage = ""
        for asset in self.__storage:
            str_storage += f"{asset.get_name()} \n"
        return (f"{self.__name} \n"
                f"{self.__broken_state} \n"
                f"{self.__upgrade_level} \n"
                f"{str_storage} \n")


"""
File: main.py
Description: This module holds the test code for the assessment.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig


# Tests that the string conversion method for both encrypted and decrypted for assets
def asset_test():
    asset = Asset("CryptoToken", "Used to acquire or repair rigs.")
    print(asset)
    asset.set_encrypted(True)
    print(asset)


def test_rig_repair():
    nix = Hacker("Nix")
    nix.acquire_rig("Nova")
    nix.repair_rig()
    titanium = Rig("Titanium")
    nix.launch_data_spike("Titanium")
    print(titanium)


# Test the store and retrieve methods
# Shows the cases of it an asset is not in storage and inventory
def test_store_and_retrieve():
    nix = Hacker("Nix")
    nix.acquire_rig("Nova")
    print(nix)
    nix.retrieve_asset(Asset("CryptoToken", ""))
    nix.retrieve_asset(Asset("Data Spike", "Used in battles."))
    print(nix)
    nix.store_asset(Asset("CryptoToken", "Used to acquire or repair rigs."))
    nix.store_asset(Asset("Data Spike", "Used in battles."))
    print(nix)

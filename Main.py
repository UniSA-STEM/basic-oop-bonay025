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


# Tests that the string conversion method for both encrypted
# #and decrypted for assets
def asset_test():
    asset = Asset("CryptoToken",
                  "Used to acquire or repair rigs.")
    print(asset)
    asset.set_encrypted(True)
    print(asset)


# Test the store and retrieve methods
# Shows the cases of it an asset is not in storage and inventory
# Shows the case of an asset being encrypted
def test_store_and_retrieve():
    nix = Hacker("Nix")
    nova = Rig("Nova")
    nix.acquire_rig(nova)
    print(nix)
    nix.retrieve_asset(Asset("CryptoToken",
                             "Used to acquire or repair rigs."))
    nix.retrieve_asset(Asset("Data Spike",
                             "Used in battles."))
    nix.encrypt_asset(Asset("Data Spike",
                            "Used in battles."))
    print(nix)
    nix.store_asset(Asset("CryptoToken",
                          "Used to acquire or repair rigs."))
    nix.store_asset(Asset("Data Spike",
                          "Used in battles."))
    print(nix)


# Tests the generation of assets
def test_generate_assets():
    nova = Rig("Nova")
    nova.generate_asset()
    print(nova)


# Test the scan inventory method
# Test case of item not being in inventory
def test_scan_inventory():
    nix = Hacker("Nix")
    nova = Rig("Nova")
    nix.acquire_rig(nova)
    nix.scan_inventory(Asset("Data Spike",
                             "Used in battles."))
    nix.retrieve_asset(Asset("Data Spike",
                             "Used in battles."))
    print(nix)
    nix.scan_inventory(Asset("Data Spike",
                             "Used in battles."))


# Tests the upgrade method
def test_upgrade_rig():
    nix = Hacker("Nix")
    nix.upgrade_rig()
    nova = Rig("Nova")
    nix.acquire_rig(nova)
    nix.upgrade_rig()
    nova.generate_asset()
    nix.retrieve_asset(Asset("Hardware Patch",
                             "Used to upgrade rigs."))
    nix.upgrade_rig()
    print(nova)


# Tests the repair method
def test_repair():
    nix = Hacker("Nix")
    nova = Rig("Nova")
    nix.acquire_rig(nova)

    zion = Hacker("Zion")
    titanium = Rig("Titanium")
    zion.acquire_rig(titanium)

    nix.launch_data_spike(titanium)
    nix.launch_data_spike(titanium)
    nix.launch_data_spike(titanium)
    print(titanium)

    zion.repair_rig()
    print(titanium)


# Test when a hackers trace level is > 5 that
# launch data spike does not work
def test_trace_level():
    nix = Hacker("Nix")
    nova = Rig("Nova")
    nix.acquire_rig(nova)
    nix.increase_trace_level()
    nix.increase_trace_level()
    nix.increase_trace_level()
    nix.increase_trace_level()
    nix.increase_trace_level()
    nix.increase_trace_level()
    print(nix)

    zion = Hacker("Zion")
    titanium = Rig("Titanium")
    zion.acquire_rig(titanium)
    nix.launch_data_spike(titanium)


# Test the encryption method
def test_encrypt():
    nix = Hacker("Nix")
    nova = Rig("Nova")
    nix.acquire_rig(nova)
    nix.encrypt_asset(Asset("Removable Drive",
                            "Found in Rigs and used for extraction."))

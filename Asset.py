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
        self.name = name
        self.description = description
        self.encrypted = False

    def __str__(self):
        if not self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"
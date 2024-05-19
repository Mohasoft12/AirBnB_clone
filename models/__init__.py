#!/usr/bin/python3

"""
Module initializer for global (singleton) variables and initialization routines.
"""

import os
from .engine.file_storage import FileStorage

# Global instance of FileStorage
storage = FileStorage()

def initialize_storage():
    """
    Initializes the global FileStorage instance.
    Attempts to reload data from a JSON file.
    """
    try:
        storage.reload()
    except FileNotFoundError:
        # Handle if the JSON file doesn't exist yet
        print("Warning: Initial JSON file not found. Starting with empty storage.")

# Main script execution
if __name__ == "__main__":
    initialize_storage()

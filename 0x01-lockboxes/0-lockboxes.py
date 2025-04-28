#!/usr/bin/python3
"""
Module for the canUnlockAll method.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list
        contains keys (integers) to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    # Keep track of boxes we can open
    unlocked = [False] * n
    # First box is already unlocked
    unlocked[0] = True
    # Keys we have available
    keys = boxes[0].copy()

    # Process keys until we have no more new keys to try
    i = 0
    while i < len(keys):
        key = keys[i]
        # Check if the key opens a valid box that we haven't opened yet
        if key < n and not unlocked[key]:
            unlocked[key] = True
            # Add new keys from this box to our collection
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)
        i += 1

    # Check if all boxes are unlocked
    return all(unlocked)

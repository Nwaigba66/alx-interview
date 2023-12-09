#!/usr/bin/python3
"""This module define a single function canUnlockAll
The function finds if a group of Box can all be
opened by accessing the first box
"""


def canUnlockAll(boxes):
    """An algorithm that check if all box in boxescan be opened

    Arguments:
    =========
    boxes (list of list): each list represents a box

    Returns (boolean): True if all every box can be accessed
    """

    found_keys = []  # found but not accessed
    accessed_keys = set()  # found and accessed
    accessed_keys.add(0)

    for key in boxes[0]:
        if key != 0:
            found_keys.append(key)

    while found_keys:  # there are unaccessed keys
        key = found_keys[0]
        found_keys = found_keys[1:]
        accessed_keys.add(key)

        for key in boxes[key]:
            if key not in accessed_keys:
                found_keys.append(key)

    return len(boxes) == len(accessed_keys)

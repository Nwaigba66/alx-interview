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
    # Set to keep track of opened boxes
    opened_boxes = {0}
    
    # List to store keys found in the process
    keys_to_process = boxes[0]
    
    while keys_to_process:
        current_key = keys_to_process.pop()
        
        # Check if the key corresponds to a valid box
        if 0 <= current_key < len(boxes) and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_to_process.extend(boxes[current_key])
    
    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)

#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of list of int): A list of lists where each list contains keys
                                  to open other boxes.
    
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:  # If there are no boxes, return True
        return True
    
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes  # Track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with the keys in the first box
    open_count = 1  # Count of opened boxes
    
    while keys:
        new_keys = []  # Store new keys found in this iteration
        for key in keys:
            if key < num_boxes and not unlocked[key]:  # Check if the box can be unlocked
                unlocked[key] = True  # Unlock the box
                open_count += 1  # Increment opened box count
                new_keys.extend(boxes[key])  # Collect new keys from the unlocked box
        
        keys = new_keys  # Update keys to explore the new keys found
        
    return open_count == num_boxes  # Check if all boxes are opened



#!/usr/bin/python3
"""
A function to check if all boxes can be opened
"""


def canUnlockAll(boxes):
    box_opened = set()  # tracks opened boxes
    box_to_open = [0]  # starts with box 0

    while box_to_open:
        current_box = box_to_open.pop()

        # Pops from box_to_open and return to current_box
        if current_box not in box_opened:
            box_opened.add(current_box)

            # Add all keys found in current_box to box_to_open
            for key in boxes[current_box]:
                if key < len(boxes) and key not in box_opened:
                    box_to_open.append(key)

    # check if all boxes are opened
    return len(box_opened) == len(boxes)

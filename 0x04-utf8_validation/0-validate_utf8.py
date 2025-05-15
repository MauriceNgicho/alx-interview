#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Checks if a given list of integers is a valid UTF-8 encoding."""
    n_bytes = 0

    for num in data:
        # Only keep the last 8 bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count how many leading 1's there are
            if (byte >> 7) == 0b0:
                continue  # 1-byte character
            elif (byte >> 5) == 0b110:
                n_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                n_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                n_bytes = 3  # 4-byte character
            else:
                return False  # Invalid first byte
        else:
            # Check that byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0

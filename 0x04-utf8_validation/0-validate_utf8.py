#!/usr/bin/python3
"""
Method to determine if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    - data: A list of integers representing the bytes of the encoding

    Returns:
    - True if the data is a valid UTF-8 encoding, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    bytes_to_process = 0

    # Masks to check the bit patterns
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # We only care about the 8 least significant bits
        byte = byte & 0xFF

        # If we are not processing any UTF-8 character
        if bytes_to_process == 0:
            # Count the number of 1s before the first 0 in the byte
            # This determines how many bytes the UTF-8 character has
            mask = 1 << 7
            while byte & mask:
                bytes_to_process += 1
                mask >>= 1

            # For a 1-byte character, the first bit should be 0
            # For multi-byte characters, the count should be between 2 and 4
            if bytes_to_process == 0:
                continue
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False

            # We've counted the number of bytes in the current character,
            # but we've already processed the first byte
            bytes_to_process -= 1
        else:
            # For continuation bytes, the bit pattern should be 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            bytes_to_process -= 1

    # All characters must be fully processed
    return bytes_to_process == 0

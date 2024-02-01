#!/usr/bin/python3

"""
Determines if a given data set represents a valid UTF-8 encoding.
"""

from typing import List

def valid_utf8(data: List[int]) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of continuation bytes for the current UTF-8 character
    continuation_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if 128 <= byte <= 191:
            if continuation_bytes == 0:
                # If there is no corresponding start byte, it's invalid
                return False
            continuation_bytes -= 1
        else:
            # Check for the number of continuation bytes based on the first byte
            if continuation_bytes > 0:
                return False
            if byte < 128:
                # ASCII character, no continuation bytes expected
                continue
            elif byte < 192:
                # Invalid start byte, as it should be followed by a continuation byte
                return False
            elif byte < 224:
                continuation_bytes = 1
            elif byte < 240:
                continuation_bytes = 2
            elif byte < 248:
                continuation_bytes = 3
            else:
                # Invalid start byte, as UTF-8 supports up to 4-byte characters
                return False

    return continuation_bytes == 0



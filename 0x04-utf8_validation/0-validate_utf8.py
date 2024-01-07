#!/usr/bin/python3
"""This module determines if a given data set represents
a valid UTF-8 encoding
The function Returns True if data is a valid UTF-8 encoding,
else return False
"""


def validUTF8(data):
    """Checks if data is correctly encoded in utf8
    """

    try:
        bytes(data)
        return True
    except Exception:
        return False

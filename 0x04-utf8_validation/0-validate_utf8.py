def validUTF8(data):
    # Helper function to check if a given byte is a valid start
    def is_start_of_utf8(byte):
        return (byte & 0b10000000) == 0b00000000

    # Helper function to check if a given byte is a continuation byte in UTF-8
    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through the data
    i = 0
    while i < len(data):
        current_byte = data[i]

        # Check for the number of bytes in the current UTF-8 character
        if is_start_of_utf8(current_byte):
            num_bytes = 1
        elif (current_byte & 0b11100000) == 0b11000000:
            num_bytes = 2
        elif (current_byte & 0b11110000) == 0b11100000:
            num_bytes = 3
        elif (current_byte & 0b11111000) == 0b11110000:
            num_bytes = 4
        else:
            # Invalid start of a UTF-8 character
            return False

        # Check the following bytes (if any) for validity
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not is_continuation_byte(data[i]):
                # Not enough continuation bytes or invalid continuation byte
                return False

        # Move to the next character
        i += 1

    # All checks passed, the data is a valid UTF-8 encoding
    return True

#!/usr/bin/python3
"""This module define a script that parses log read from standard input
"""
import sys
import signal

# Initialize variables
total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

# Function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Function to print statistics
def print_stats():
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read input lines from stdin
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()

        # Check if the line follows the specified format
        if len(parts) >= 7 and parts[5].isdigit():
            ip_address, date, status_code, file_size = parts[0], parts[3][1:], int(parts[6]), int(parts[9])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            # Increment the lines processed counter
            lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()


#!/usr/bin/python3
import sys


total_size = 0
line_count = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


def stats_print(total_size, status_counts):
    """Prints the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()  # Removes the new line
        parts = line.split()  # Split line to indexes

        #  Skip invalid lines
        if len(parts) < 7:
            continue

        #  Try to extract the status code and file size
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        #  Accumulate total file size
        total_size += file_size

        #  Convert status codes to str for consistency with the valid codes
        code_str = str(status_code)

        #  Count valid status codes
        if code_str in valid_codes:
            if code_str in status_counts:
                status_counts[code_str] += 1
            else:
                status_counts[code_str] = 1

        line_count += 1
        if line_count % 10 == 0:
            stats_print(total_size, status_counts)

except KeyboardInterrupt:
    stats_print(total_size, status_counts)
    raise

stats_print(total_size, status_counts)

#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re


def print_stats(total_size, status_codes):
    """
    Print statistics including total file size and count of status codes.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_codes.keys()):
        if status_codes[status] > 0:
            print(f"{status}: {status_codes[status]}")


def main():
    """
    Main function to process input and compute metrics.
    """
    # Regular expression to match the expected line format
    line_pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    
    # Initialize variables
    total_size = 0
    line_count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    
    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(line_pattern, line)
            
            if match:
                # Extract status code and file size
                status_code = int(match.group(3))
                file_size = int(match.group(4))
                
                # Update metrics
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                # Increment line count
                line_count += 1
                
                # Print stats after every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
    
    except KeyboardInterrupt:
        # Handle CTRL+C interruption
        pass
    
    finally:
        # Print stats one last time before exiting
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

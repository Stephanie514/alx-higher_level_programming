#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size and count of read status
"""

def print_metrics(total_size, status_code_counts):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated total file size.
        status_code_counts (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(total_size))
    for code in sorted(status_code_counts):
        print("Status code {}: {}".format(code, status_code_counts[code]))

if __name__ == "__main__":
    import sys

    total_size = 0
    status_code_counts = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line_parts = line.split()

            try:
                file_size = int(line_parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = line_parts[-2]
                if status_code in valid_status_codes:
                    status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
            except IndexError:
                pass

            if line_count == 10:
                print_metrics(total_size, status_code_counts)
                line_count = 0

        print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code_counts)
        raise

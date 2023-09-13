#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {:d}".format(size))
    for key in sorted(status_codes):
        print("{}: {:d}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            try:
                elements = line.split()
                code = elements[-2]
                size += int(elements[-1])

                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except (ValueError, IndexError):
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

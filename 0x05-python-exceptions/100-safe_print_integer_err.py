#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("Exception: Not a valid integer", file=sys.stderr)
        return False

#!/usr/bin/python3

def safe_print_integer(value):
    try:
        form_val = "{:d}".format(value)
        print(form_val)
        return True
    except (ValueError, TypeError):
        return False

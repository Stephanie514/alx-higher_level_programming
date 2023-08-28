#!/usr/bin/python3

def safe_print_integer(value):
    try:
        form_val = "{:d}".format(int(value))
        print(form_val)
        return True
    except ValueError:
        return False

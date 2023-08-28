#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        ans = a / b
    except (ZeroDivisionError, FloatingPointError):
        ans = None
    finally:
        try:
            print("Inside result: {}".format(ans))
        except NameError:
            print("Inside result: {}".format(None))
            return None
        return ans

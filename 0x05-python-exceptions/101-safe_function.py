#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        output = fct(*args)
    except Exception as g:
        print("Exception:", g, file=sys.stderr)
        output = None
    return output

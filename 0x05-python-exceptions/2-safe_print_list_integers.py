#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ttl = 0
    try:
        for a in range(x):
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                ttl += 1
        print()
    except IndexError:
        raise
    except (ValueError, TypeError):
        pass
    return ttl

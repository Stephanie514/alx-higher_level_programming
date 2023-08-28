#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ttl = 0
    cnt = 0

    try:
        while cnt < x:
            if isinstance(my_list[cnt], int):
                print("{:d}".format(my_list[cnt]), end="")
                ttl += 1
            cnt += 1
    except (ValueError, TypeError, IndexError):
        pass

    print()
    return ttl

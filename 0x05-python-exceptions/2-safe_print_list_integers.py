#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ttl = 0
    cnt = 0

    while cnt < x:
        try:
            product = my_list[cnt]
            if isinstance(product, int):
                print("{:d}".format(product), end="")
                ttl += 1
            cnt += 1
        except (ValueError, TypeError, IndexError):
            break

    print()
    return ttl

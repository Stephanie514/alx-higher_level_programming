#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total_printed = 0
    while total_printed < x:
        try:
            print(my_list[total_printed], end="")
            total_printed += 1
        except IndexError:
            break
    print()
    return total_printed

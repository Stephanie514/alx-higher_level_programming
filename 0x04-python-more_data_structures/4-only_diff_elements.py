#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_dif = set()

    for item in set_1:
        if item not in set_2:
            set_dif.add(item)

    for item in set_2:
        if item not in set_1:
            set_dif.add(item)

    return set_dif

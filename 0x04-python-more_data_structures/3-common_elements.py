#!/usr/bin/python3

def common_elements(set_1, set_2):
    similar_set = set()

    for item in set_1:
        if item in set_2:
            similar_set.add(item)

    return similar_set

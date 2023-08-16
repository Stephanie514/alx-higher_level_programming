#!/usr/bin/python3

def uniq_add(my_list=[]):
    the_list = set(my_list)
    ttl_sum = 0

    for num in the_list:
        ttl_sum += num

    return ttl_sum

#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    ttl_wt = 0
    ttl_product = 0

    for value, weight in my_list:
        ttl_wt += weight
        ttl_product += value * weight

    return ttl_product / ttl_wt

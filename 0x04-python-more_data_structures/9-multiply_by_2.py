#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    another_dict = {}

    for key, value in a_dictionary.items():
        new_value = value * 2
        another_dict[key] = new_value

    return another_dict

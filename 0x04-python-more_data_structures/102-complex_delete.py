#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_rem = [key for key, val in a_dictionary.items() if val == value]

    for key_remove in keys_rem:
        del a_dictionary[key_remove]

    return a_dictionary

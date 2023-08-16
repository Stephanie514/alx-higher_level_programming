#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    total = roman_values[roman_string[-1]]

    for i in range(len(roman_string) - 2, -1, -1):
        curr_value = roman_values[roman_string[i]]
        next_value = roman_values[roman_string[i + 1]]
        total += curr_value if curr_value >= next_value else -curr_value

    return total

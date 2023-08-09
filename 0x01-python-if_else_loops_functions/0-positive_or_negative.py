#!/usr/bin/python3
import random

number = random.randint(-10, 10)


def print_number_classification(number):

    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")


print_number_classification(number)

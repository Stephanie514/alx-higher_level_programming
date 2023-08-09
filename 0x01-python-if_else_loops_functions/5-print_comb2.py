#!/usr/bin/python3

# 4-print_0to99.py

"""Print numbers from 0 to 99."""

for number in range(100):
    print("{:02}".format(number), end=", " if number < 99 else "\n")

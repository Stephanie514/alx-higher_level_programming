#!/usr/bin/python3

# 100-print_tebahpla.py

"""Print the alphabet in reverse order alternating upper- and lower-case."""

for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - (ord('a') - ord('A')) * (c % 2))), end="")

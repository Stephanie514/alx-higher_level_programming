#!/usr/bin/python3

# 100-print_tebahpla.py

"""Print the alphabet in reverse order alternating upper- and lower-case."""

for c in range(ord('z'), ord('a') - 1, -1):
    print(chr(c - 32 * (c % 2)), end="")

#!/usr/bin/python3

# 100-print_tebahpla.py

"""Print the alphabet in reverse order alternating lower- and upper-case."""

for offset in range(25, -1, -1):
    print("{}".format(chr(ord('a') + offset)), end="")
    print("{}".format(chr(ord('A') + offset)), end="") if offset % 2 == 0 else None

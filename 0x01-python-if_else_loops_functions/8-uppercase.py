#!/usr/bin/python3

# 8-uppercase.py

def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end="")
        else:
            print("{}".format(char), end="")
    print()

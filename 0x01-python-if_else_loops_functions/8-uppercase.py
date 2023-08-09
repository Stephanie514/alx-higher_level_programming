#!/usr/bin/python3

# 8-uppercase.py

def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - ord('a') + ord('A')), end="")
        else:
            print(char, end="")
    print()

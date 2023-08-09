#!/usr/bin/python3

# 8-uppercase.py

def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)

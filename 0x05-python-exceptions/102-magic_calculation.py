#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0
    v = 1
    while v < 3:
        try:
            if v > a:
                raise Exception('Too far')
            else:
                output += a ** b / v
        except Exception:
            output = b + a
            break
        v += 1
    return output 

#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

result = "greater than 5" if last_digit > 5 else "0" if last_digit == 0 else "less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} and is {result}")


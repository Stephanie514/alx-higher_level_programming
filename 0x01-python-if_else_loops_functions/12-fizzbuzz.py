#!/usr/bin/python3

# 12-fizzbuzz.py

def fizzbuzz():
    """Print numbers from 1 to 100 following FizzBuzz rules."""
    for number in range(1, 101):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        print(output or number, end=" ")

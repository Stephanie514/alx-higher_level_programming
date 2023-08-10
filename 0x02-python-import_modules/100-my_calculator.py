#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    value_a, operator, value_b = map(str.strip, sys.argv[1:])

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    value_a, value_b = map(int, (value_a, value_b))
    result = operators[operator](value_a, value_b)

    print(f"{value_a} {operator} {value_b} = {result}")

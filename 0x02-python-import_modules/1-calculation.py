#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    res = {
        "add": add(a, b),
        "sub": sub(a, b),
        "mul": mul(a, b),
        "div": div(a, b)
    }

    format_strings = {
        "add": "{} + {} = {}",
        "sub": "{} - {} = {}",
        "mul": "{} * {} = {}",
        "div": "{} / {} = {}"
    }

    for operation, result in res.items():
        print(format_strings[operation].format(a, b, result))

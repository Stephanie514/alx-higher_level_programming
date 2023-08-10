#!/usr/bin/python3

import hidden_4 as hid4

if __name__ == "__main__":
    listofnames = dir(hid4)

    for name in listofnames:
        if not name.startswith("__"):
            print(name)

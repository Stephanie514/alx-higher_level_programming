#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    another_list = []
    a = 0

    while a < list_length:
        try:
            res = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        another_list.append(res)
        a += 1

    return another_list

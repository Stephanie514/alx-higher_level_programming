#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    another_list = []
    a = 0

    while a < list_length:
        try:
            res = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except (TypeError, ValueError):
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            another_list.append(res)
            a += 1

    return another_list

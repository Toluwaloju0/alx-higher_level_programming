#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None or my_list_2 is None:
        return None
    try:
        new_list = [0] * list_length
        a = 0
        for a in range(list_length):
            if not isinstance(my_list_2[a], (int, float)):
                print("wrong type")
                continue
            if not isinstance(my_list_2[a], (int, float)):
                print("wrong type")
                continue
            if my_list_2[a] == 0:
                print("division by 0")
                continue
            new_list[a] = my_list_1[a] / my_list_2[a]
    except IndexError:
        print("out of range")
    finally:
        return new_list

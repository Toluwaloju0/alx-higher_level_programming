#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    if my_list_1 or my_list_2 is None:
        return None
    try:
        a = 0
        while a < list_length:
            new_list[a] = (my_list_1[a] / my_list_2[a])
            a += 1
    except IndexError:
        print("out of range")
        pass
    except ZeroDivisionError: 
        print("division by 0")
        pass
    except TypeError:
        print("wrong type")
        pass
    return new_list

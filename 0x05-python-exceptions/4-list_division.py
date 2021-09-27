#!/usr/bin/python3


def list_division(my_list1, my_list2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list1[i] / my_list2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list
#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range (list_length):
        l = 0
        try:
            l = (my_list_1[i]/my_list_2[i])
        except(ZeroDivisionError):
            print("division by 0")
        except(TypeError):
            print("wrong type")
        except(IndexError):
            print("out of range")
        finally:
            my_list_3.append(l)
    return (my_list_3)
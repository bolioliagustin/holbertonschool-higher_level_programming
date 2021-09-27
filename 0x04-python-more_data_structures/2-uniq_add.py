#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma_lista = 0
    new_string = set(my_list)
    new_list = list(new_string)
    for i in new_list:
        suma_lista += i
    return(suma_lista)

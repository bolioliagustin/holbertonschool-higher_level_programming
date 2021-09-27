#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = (number * -1)
    number2 = number % 10
    print("{}".format(number2), end="")
    return number2

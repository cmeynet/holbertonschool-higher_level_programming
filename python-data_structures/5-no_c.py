#!/usr/bin/python3
def no_c(my_string):
    temp_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            temp_string += my_string[i]
    return temp_string

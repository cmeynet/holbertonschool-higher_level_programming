#!/usr/bin/python3
"""
This is the "1-my_list" modulo.
Its contains the function: print_sorted
and the class: MyList
"""


class MyList(list):
    """ Class MyList that inherits from list """

    def print_sorted(self):
        """
        Function that prints a list, sorted in ascending order
        """
        print(sorted(self))

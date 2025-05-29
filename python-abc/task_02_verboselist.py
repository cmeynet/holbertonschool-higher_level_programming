#!/usr/bin/python3
"""
This is the "task_02_verboselist" modulo.
Its contains the class:
VerboseList
"""


class VerboseList(list):
    """
    Defines a VerboseList

    Methods:
    append: append an item to the end of the list
    extend: extend the list by appending all the items from the iterable
    remove: remove the first item from the list
    pop: remove the item at the given position in the list
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

#!/usr/bin/python3
"""
This is the "task_03_countediterator" modulo.
Its contains the class:
CountedIterator
"""


class CountedIterator:
    """Defines a CountedIterator"""
    def __init__(self, iterator, counter=0):
        self.counter = counter
        self.iterator = iter(iterator)

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

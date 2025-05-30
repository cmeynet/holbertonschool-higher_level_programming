#!/usr/bin/python3
"""
This is the "task_03_countediterator" modulo.
Its contains the class:
CountedIterator
"""


class Fish:
    """ Defines a Fish """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """ Defines a Bird """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """ Defines a FlyingFish that inherates from Fish and Bird """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

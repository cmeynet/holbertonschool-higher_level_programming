#!/usr/bin/python3
"""
This is the "task_05_dragon" modulo.
Its contains the class:
SwimMixin, FlyMixin, Dragon
"""


class SwimMixin:
    """ Defines a SwimMixin """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """ Defines a FlyMixin """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ Defines a Dragon that inherates from SwimMixin and FlyMixin """
    def roar(self):
        print("The dragon roars!")

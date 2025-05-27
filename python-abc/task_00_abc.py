#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This is the "task_00_abc" modulo.
Its contains the abstract class:
Animal
and the subclasses:
Dog, Cat
"""


class Animal(ABC):
    """
    Defines a Animal

    Abstract method:
        sound: the sound of the animal
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Defines a Dog

    Method:
        sound: the sound of the animal
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Defines a Cat

    Method:
        sound: the sound of the animal
    """
    def sound(self):
        return "Meow"

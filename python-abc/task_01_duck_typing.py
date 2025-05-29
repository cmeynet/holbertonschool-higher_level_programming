from abc import ABC, abstractmethod
import math
"""
This is the "task_00_abc" modulo.
Its contains the abstract class:
Shape
and the subclasses:
Circle, Rectangle
"""


class Shape(ABC):
    """
    Define a Shape

    Abstract method:
    area: the area of the shape
    perimeter: the perimeter of the shape
    """
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """Defines a circle"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.radius * math.pi


class Rectangle(Shape):
    """Defines a rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


def shape_info(thing):
    print("Area: {}".format(thing.area()))
    print("Perimeter: {}".format(thing.perimeter()))

#!/usr/bin/python3
"""
contains 'Square' class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class that represents a square geometric shape
    inherits from 'Rectangle' class
    """
    def __init__(self, size):
        self.integer_validator('size', size)
        self._width = self._height = size

    def area(self):
        return self._width ** 2

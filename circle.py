"""A small Circle class for a student technical-writing assignment."""

import math


class Circle:
    """Represent a circle using its radius.

    Known issue: the constructor does not check that the radius is greater
    than zero. Positive-radius validation is planned but not implemented.
    """

    def __init__(self, radius):
        self._radius = radius

    def getRadius(self):
        """Return the radius supplied when the circle was created."""
        return self._radius

    def getDiameter(self):
        """Return the diameter: twice the radius."""
        return 2 * self._radius

    def getArea(self):
        """Return the area: pi times the radius squared."""
        return math.pi * self._radius ** 2

    def getCircumference(self):
        """Return the distance around the circle: twice pi times the radius."""
        return 2 * math.pi * self._radius

    def __str__(self):
        return (
            "Circle details:\n"
            f"  Radius: {self.getRadius()}\n"
            f"  Diameter: {self.getDiameter()}\n"
            f"  Area: {self.getArea()}\n"
            f"  Circumference: {self.getCircumference()}"
        )

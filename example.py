"""Demonstrate each Circle method and printing a Circle instance."""

from circle import Circle


def main():
    circleInstance = Circle(5)

    print("getRadius():", circleInstance.getRadius())
    print("getDiameter():", circleInstance.getDiameter())
    print("getArea():", circleInstance.getArea())
    print("getCircumference():", circleInstance.getCircumference())
    print()
    print(circleInstance)


if __name__ == "__main__":
    main()

#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Square(width={self.width}, height={self.height})"


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

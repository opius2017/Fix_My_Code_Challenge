#!/usr/bin/python3

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """Calculate the area of the square"""
        return self.side_length ** 2

    def perimeter(self):
        """Calculate the perimeter of the square"""
        return 4 * self.side_length

    def __str__(self):
        return f"Square: side length={self.side_length}"

if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

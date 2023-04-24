#!/usr/bin/env python3

import math

class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def __str__(self):
        return "Ellipse(" + str(self.a) + ", " + str(self.b) + ")"

    def __repr__(self):
        return "Ellipse(" + str(self.a) + ", " + str(self.b) + ")"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


class Sphere(Ellipse):
    def __init__(self, r):
        super().__init__(r, r)

    def __str__(self):
        return "Sphere(" + str(self.a) + ")"

    def __repr__(self):
        return "Sphere(" + str(self.a) + ")"

    def __eq__(self, other):
        return self.a == other.a

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


def main():
    e1 = Ellipse(10, 20)
    e2 = Ellipse(20, 10)
    e3 = Ellipse(10, 20)
    print(e1 == e2)  # False
    print(e1 == e3)  # True
    print(e1 < e2)   # True
    print(e1 <= e2)  # True
    print(e1 > e2)   # False
    print(e1 >= e2)  # False
    print(e1 < e3)   # False
    print(e1 <= e3)  # True
    print(e1 > e3)   # False
    print(e1 >= e3)  # True
    print(e1)        # Ellipse(10, 20)
    print(e2)        # Ellipse(20, 10)
    print(e3)        # Ellipse(10, 20)
    print("-" * 40)
    s1 = Sphere(10)
    s2 = Sphere(20)
    s3 = Sphere(10)
    print(s1 == s2)  # False
    print(s1 == s3)  # True
    print(s1 < s2)   # True
    print(s1 <= s2)  # True
    print(s1 > s2)   # False
    print(s1 >= s2)  # False
    print(s1 < s3)   # False
    print(s1 <= s3)  # True
    print(s1 > s3)   # False
    print(s1 >= s3)  # True
    print(s1)        # Sphere(10)
    print(s2)        # Sphere(20)
    print(s3)        # Sphere(10)


if __name__ == "__main__":
    main()

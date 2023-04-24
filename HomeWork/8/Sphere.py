
#Sphere (gömb) és Ellipse (ellipszis) osztályok megírása; a Sphere osztály esetén terheljük túl a következő operátorokat: <, <=, >, >= .
import math

class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def __str__(self):
        return "Ellipse(" + str(self.a) + ", " + str(self.b) + ")"


class Sphere():
    def __init__(self, r):
        super().__init__(r, r)

    def area(self):
        return 4 * math.pi * self.a ** 2
    def __str__(self):
        return "Sphere(" + str(self.a) + ")"


def main():
    e1 = Ellipse(10, 20)
    e2 = Ellipse(20, 10)
    e3 = Ellipse(10, 20)

    print(e1)        # Ellipse(10, 20)
    print(e2)        # Ellipse(20, 10)
    print(e3)        # Ellipse(10, 20)
    print("-" * 20)
    s1 = Sphere(10)
    s2 = Sphere(20)
    s3 = Sphere(10)

    print(s1)        # Sphere(10)
    print(s2)        # Sphere(20)
    print(s3)        # Sphere(10)


if __name__ == "__main__":
    main()
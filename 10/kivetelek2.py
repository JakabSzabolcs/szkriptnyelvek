#!/usr/bin/env python3
import sys


# sajat kivetel
class MyException(Exception):
    raise IOError


def main():
    while True:
        szam1 = float(input("1. szam: "))
        szam2 = float(input("2. szam: "))
        try:
            result = szam1 / szam2
        except ZeroDivisionError:
            print("Nullával való osztás nem lehetséges!")
            exit()
        else:
            print("Az osztas eredmenye: {0:.2f}".format(result))
            print("-"*10)

        finally:
            print("A program lefutott!")


#####


if __name__ == "__main__":
    main()

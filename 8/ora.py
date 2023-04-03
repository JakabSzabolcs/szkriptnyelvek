#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Allatok:
    pass


class Cica(Allatok):

    def Meow(self):
        return "Miau"


class Hello:

    def create_name(self, name):
        self.name = name


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)

    def __str__(self) -> str:
        return str(self.data)


def main():
    kisCica = Cica()
    print(kisCica.Meow())
    b = Bag()
    b.add(1)
    b.add(2)
    b.add('Cica')
    print(b)


if __name__ == '__main__':
    main()

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


def main():
    kisCica = Cica()
    print(kisCica.Meow())


if __name__ == '__main__':
    main()

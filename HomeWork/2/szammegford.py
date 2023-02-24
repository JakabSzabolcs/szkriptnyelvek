#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Írjunk függvényt, mely kap egy pozitív egész számot, s visszatérési értékként a szám fordítottját adja vissza mint egész számot.


def szammegford(n):
    n = str(n)
    n = n[::-1]
    return int(n)

if __name__ == '__main__':
    print(szammegford(1234))
    print(szammegford(56789))
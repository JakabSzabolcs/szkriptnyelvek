#!/usr/bin/env python3
from sys import argv
import sys


def karakter_szamlalo(sztring):
    szotar = {}
    for karakter in sztring:
        if karakter in szotar:
            szotar[karakter] += 1
        else:
            szotar[karakter] = 1

    return szotar


def main():
    if len(argv) != 2:
        print(
            "Hiba! A program csak egy parancssori argumentumot fogad el!", file=sys.stderr)
        exit()
    eredmeny = karakter_szamlalo(argv[1])
    for par in eredmeny:
        print(par, "-", eredmeny[par])


if __name__ == "__main__":
    main()

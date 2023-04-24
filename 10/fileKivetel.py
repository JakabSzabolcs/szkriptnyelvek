#!/usr/bin/env python3

import sys


def cat(fname):
    try:
        f = open(fname, "r")
        text = f.read()
        print("---", fname)
        print(text)
        f.close()
    # Konkrét kivétel
    # except FileNotFoundError:
    #   print("Nincs ilyen fájl:", fname)
    # Kivétel családok
    except IOError as e:
        print("Hiba! File kezelési hiba történt : ", fname, "\n ErrorCode:", e)


def main():
    args = sys.argv[1:]
    for arg in args:
        cat(arg)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tuple adatszerkezet (immutable) - nem lehet megvaltoztatni


# a = (1, 2, 3)
# print(a)
# print(a[0])

# # a[0] = 2  # TypeError: 'tuple' object does not support item assignment
# movie = ("Total recall", 1990, 7.5)
# # tuple-lel lehet párhuzamos értékadást is csinálni
# x, y, z = movie
# print(x, y, z)
# # egy = ("cica",)  # ha csak egy elemu tuple-t akarunk, akkor kell a vesszo")


def main():
    title, year, rating = ("Total recall", 1990, 7.5)
    print(title, year, rating)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# String Formatting

# Text alignment
#  '^' - for center alignment
#  '<' - for left alignment
#  '>' - for right alignment


def HaladoStringformazas():
    lang_info = [('Fortran', 1954, 0.435), ('Cobol', 1959, 0.391),
                 ('C', 1972, 16.076), ('C++', 1980, 9.014),
                 ('Python', 1991, 6.482),
                 ('Java', 1995, 17.99), ('C#', 2001, 6.687)]
    print(lang_info)

    print('Formázás követően:')
    print(f"{0:<12} {1:^16} {2:>16}".format("Language",
                                            "Year Developed",
                                            "TIOBE rating"))
    print("*"*50)
    for element in lang_info:
        print(f"{0:12} {1:^16} {2:16}".format(
            element[0], element[1], element[2]))

    starters = [
        ['Andre Iguodala', 4, 3, 7],
        ['Klay Thompson', 5, 0, 21],
        ['Stephen Curry', 5, 8, 36],
        ['Draymon Green', 9, 4, 11],
        ['Andrew Bogut', 3, 0, 2],
    ]

    # Szám formázás táblázatba
    row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:2d} |".format

    for p in starters:
        print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3]))


if __name__ == '__main__':
    HaladoStringformazas()

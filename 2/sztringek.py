#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sztringek concatenation-ja a "+" operátorral történik
# Sztringekben való kereséséhez a "find()" metódust használjuk
# Sztingek hosszát a "len()" metódussal tudjuk meghatározni
# A "replace()" metódussal tudunk sztringeket cserélni
# A "split()" metódussal tudunk sztringeket szétválasztani
# A "join()" metódussal tudunk sztringeket összefűzni
# A "strip()" metódussal tudjuk a whitespace karaktereket eltávolítani az elejéről és végéről
# A "iswhitespace()" metódussal tudjuk megnézni, hogy a sztring csak whitespace karaktereket tartalmaz-e
# A "isaaplha()" metódussal tudjuk megnézni, hogy a sztring csak betűket tartalmaz-e

def main():
    hello("szabi", "fekete", "ég")


def hello(name, color, what):
    # 1
    print("{0}, {1} a(z) {2}".format(name, color, what))
    # 2
    print("{}, {} a(z) {}".format(name, color, what))
    # 3
    print("{nev}, {szin} a(z) {mi}".format(nev=name, szin=color, mi=what))
    # 4 , Ide kifejezéseket kell írni (+plussz kis formázás)
    print(f"{name.capitalize()}, {color} a(z) {what}")
    # Stringek szétválasztása
    print(name[2:4])
    print(name[2:])
    # String backwards
    print(name[::-1])
    # Több soros string
    print("""This is a
    multi-line string""")
    # Raw string
    s = r"this is a raw string \n"  # speciális karakterek nem lesznek értelmezve


if __name__ == '__main__':
    main()

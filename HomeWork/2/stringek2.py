#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.

# További sztring műveletek


# E. verbing
# Ha az adott sztring hossza legalább 3, akkor
# a végéhez adjuk hozzá az 'ing' ragot.
# Ha 'ing'-re végződik, akkor ehelyett az 'ly'
# ragot tegyük hozzá.
# Ha a sztring hossza rövidebb 3 karakternél, akkor
# hagyjuk változatlanul.
# Adjuk vissza az eredménysztringet.

def verbing(s):
    if len(s) < 3:
        return s
    if s[-3:] == "ing":
        return s + "ly"
    return s + "ing"


# F. not_bad
# Egy adott sztringben keressük meg a 'not' és
# 'bad' szavak előfordulási helyét. Ha a 'bad'
# a 'not' szót követi, akkor cseréljük ki az
# egész 'not'...'bad' részsztringet a 'good' szóra.
# Adjuk vissza az eredmény sztringet.
# Példa: 'This dinner is not that bad!' ->
#        This dinner is good!

def not_bad(s):
    notIndex = s.find("not")
    badIndex = s.find("bad")
    if notIndex < badIndex:
        return s[:notIndex] + "good" + s[badIndex + 3:]
    return s

# G. front_back
# Egy sztringet osszunk két részre, s a két részt nevezzük
# a sztring elejének és végének. Ha a sztring hossza páros, akkor
# a két rész hossza azonos. Ha a hossz páratlan, akkor az eleje
# legyen egy karakterrel hosszabb mint a vége.
# Például 'abcde' esetén a két rész: 'abc' és 'de'.
# Két adott sztring (a és b) esetén adjunk vissza egy sztringet, mely
# a következőképpen épül fel:
# a-eleje + b-eleje + a-vége + b-vége
# Például ha a = 'abcd' és b = 'xy', akkor az eredmény 'abxcdy' legyen.

def front_back(a, b):
    aMiddle = len(a) // 2
    bMiddle = len(b) // 2
    if len(a) % 2 == 1:
        aMiddle += 1
    if len(b) % 2 == 1:
        bMiddle += 1
    return a[:aMiddle] + b[:bMiddle] + a[aMiddle:] + b[bMiddle:]

# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################

if __name__ == '__main__':
    main()
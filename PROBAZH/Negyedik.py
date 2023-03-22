#!/usr/bin/env python3
#encoding: utf-8
import sys

def main():
    if len(sys.argv) != 2:
        print("Hiba! Meg kell adni egy(!) darab parancssori argumentumot a működéshez!",f = sys.stderr)
        exit()

    if len(sys.argv[1]) < 10:
        print("Hiba! A megadott parancssori argumentum túl rövid!",f = sys.stderr)
        exit()

    if len(sys.argv[1]) > 10:
        print("Hiba! A megadott parancssori argumentum túl hosszú!",f = sys.stderr)
        exit()

    ascii = [ord(c) for c in sys.argv[1]]
    paros = [int(c * 1.5) for c in ascii if c % 2 == 0]
    paratlan = [c * (-2) for c in ascii if c % 2 != 0]

    osszefuzott = paros + paratlan
    print(osszefuzott)

if __name__ == "__main__":
    main()
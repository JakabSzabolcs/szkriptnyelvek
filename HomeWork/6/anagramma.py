#!/usr/bin/env python3
# encoding: utf-8


def anagramma(szoveg1, szoveg2):
    szoveg1 = szoveg1.lower()
    szoveg2 = szoveg2.lower()
    szoveg1 = szoveg1.replace(" ", "")
    szoveg2 = szoveg2.replace(" ", "")
    szoveg1 = sorted(szoveg1)
    szoveg2 = sorted(szoveg2)
    if szoveg1 == szoveg2:
        return True
    else:
        return False


def main():
    print(anagramma("listen", "silent"))
    print(anagramma("A gentleman", "Elegant man"))
    print(anagramma("Clint Eastwood", "Old west action"))
    print(anagramma("dormitory", "dirty room"))
    print(anagramma("The Morse Code", "Here come dots"))


if __name__ == "__main__":
    main()

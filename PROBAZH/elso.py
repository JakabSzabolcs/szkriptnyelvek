#!/usr/bin/env python3
# encoding: utf-8

def main():
    pontok = open("pontok.txt", "r")
    erdemjegyek = {
        "Egyes": [0, 1, 1.5, 2],
        "Kettes": [2],
        "Hármas": [2.5],
        "Négyes": [3],
        "Ötös": [3.5, 4]
    }

    egyesek, kettesek, harmasok, negyesek, otosok = 0, 0, 0, 0, 0

    for sor in pontok:
        pont = float(sor.split()[1])
        if pont in erdemjegyek["Egyes"]:
            egyesek += 1
        if pont in erdemjegyek["Kettes"]:
            kettesek += 1
        if pont in erdemjegyek["Hármas"]:
            harmasok += 1
        if pont in erdemjegyek["Négyes"]:
            negyesek += 1
        if pont in erdemjegyek["Ötös"]:
            otosok += 1

    print("Egyes: ", egyesek)
    print("Kettes: ", kettesek)
    print("Hármas: ", harmasok)
    print("Négyes: ", negyesek)
    print("Ötös: ", otosok)

    atlag = (egyesek * 1 + kettesek * 2 + harmasok * 3 + negyesek * 4 +
             otosok * 5) / (egyesek + kettesek + harmasok + negyesek + otosok)

    print("Átlag: ", round(atlag, 2))


if __name__ == "__main__":
    main()

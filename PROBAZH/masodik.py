#!/usr/bin/env python3

def Hangrend(szo):
    # csak angol abc betuket tartalmaz
    mely = "aou"
    magas = "ei"
    melycount = 0
    magascount = 0
    for s in szo:
        if s in mely:
            melycount += 1
        if s in magas:
            magascount += 1
    if melycount > 0 and magascount == 0:
        return 1
    elif magascount > 0 and melycount == 0:
        return 2
    elif magascount > 0 and melycount > 0:
        return 3
    else:
        return 4


def main():
    szavak = open("words.txt", "r")
    mely = 0
    magas = 0
    vegyes = 0
    for sor in szavak:
        szo = sor.strip()
        if Hangrend(szo) == 1:
            mely += 1
        elif Hangrend(szo) == 2:
            magas += 1
        elif Hangrend(szo) == 3:
            vegyes += 1
        elif Hangrend(szo) == 4:
            continue
    print("Magas hangrendű szavak - ", magas)
    print("Mély hangrendű szavak - ", mely)
    print("Vegyes hangrendű szavak - ", vegyes)


if __name__ == "__main__":
    main()

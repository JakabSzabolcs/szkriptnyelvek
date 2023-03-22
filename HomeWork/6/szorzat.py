#A következő 1000 számjegyű számban (ami az olvashatóság kedvéért tördelve lett) keressük meg öt egymást követő számjegy legnagyobb szorzatát.
#a szám a szam.txt fájlban található


def main():
    with open("szam.txt") as f:
        szam = f.read()
    szam = szam.replace("\n", "")
    szorzat = 0
    for i in range(len(szam) - 4):
        if int(szam[i]) * int(szam[i + 1]) * int(szam[i + 2]) * int(szam[i + 3]) * int(szam[i + 4]) > szorzat:
            szorzat = int(szam[i]) * int(szam[i + 1]) * int(szam[i + 2]) * int(szam[i + 3]) * int(szam[i + 4])
    print(szorzat)


if __name__ == "__main__":
    main()
#Írjanak egy a-z.py nevű szkriptet, amit lefuttatva megkapjuk az angol ábécé kisbetűit a-tól z-ig. Tegyünk egy szimbolikus linket a szkriptre z-a.py néven. A z-a.py -t futtatva viszont az angol ábécé kisbetűit fordítva szeretnénk megkapni, vagyis z-től a-ig


def main():
    return "".join([chr(i) for i in range(97, 123)])

if __name__ == "__main__":
    main()
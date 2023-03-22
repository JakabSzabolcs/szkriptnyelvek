#!/usr/bin/env python3
# Hatványozás
# 2**3 = 2*2*2

# IF ELSE ELIF elágazások


def main():
    allatok = ["kutya", "macska", "cica", "kenguru", "tigris", "medve"]
    for allat in allatok:
        # print index és elem
        print(allatok.index(allat), allat)
    print('\nEnumerate:\n')
    # enumerate
    # az enumerate opcionálisan megadható, hogy melyik indextől kezdje
    for index, allat in enumerate(allatok, start=1):
        print(index, allat)


if __name__ == "__main__":
    main()

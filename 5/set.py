#!/usr/bin/env python3

# a set egy halmaz, amiben csak egyedi elemek lehetnek
# a set() függvény létrehoz egy üres halmazt

def main():
    kosar = ['alma', 'körte', 'alma', 'szilva', 'körte']
    kosar = set(kosar)
    print(kosar)
    # kardinalitás (hány elem van a halmazban)

    li = [5, 2, 3, 5, 1, 4, -22, 5, 1, 3, 2, 2, 5]
    li = sorted(set(li))
    print(li)

    # Tipikus set() metódusok:
    # union() - egyesíti a két halmazt
    # intersection() - metszi a két halmazt
    # difference() - kivonja a második halmaz elemeit az elsőből
    # symmetric_difference() - kivonja a két halmaz közös elemeit
    # issubset() - Eldönti, hogy az első halmaz részhalmaza-e a másodiknak
    # issuperset() - Eldönti, hogy az első halmaz tartalmazza-e a másodikat
    # isdisjoint() - Eldönti, hogy két halmaznak van-e közös eleme
    # mi a különbség a discard() és a remove() között?


if __name__ == "__main__":
    main()


# ZH kérdés : mi a különbés a sorted() és a sort() között?
# A sorted() egy függvény
# A sort() egy metódus
# a sort() helyben rendez,
# a sorted() egy új listát hoz létre, és azt rendezi

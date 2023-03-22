#!/usr/bin/env python3

# Mély hangrendű magánhangzók: a, á, o, ó, u, ú.
# Magas hangrendű magánhangzók: e, é, i, í, ö, ő, ü, ű.
# Ha egy szóban vmennyi magánhangzó mély hangrendű, akkor a szó mély hangrendű. Ha egy szóban vmennyi magánhangzó magas hangrendű, akkor a szó magas hangrendű. Ha egy szóban mély és magas hangrendű magánhangzók is előfordulnak, akkor a szó vegyes hangrendű. Ha a szóban nincs egyetlen magánhangzó sem, akkor semmilyen hangrendű.

def Hangrend(szoveg):
    magas = 0
    mely = 0
    for i in szoveg:
        if i in "aáoóuú":
            mely += 1
        elif i in "eéiíöőüű":
            magas += 1
    if magas == 0:
        return "Mély hangrendű"
    elif mely == 0:
        return "Magas hangrendű"
    else:
        return "Vegyes hangrendű"


def main():
    print(Hangrend("ablak"))
    print(Hangrend("erkély"))
    print(Hangrend("tükör"))
    print(Hangrend("otthon"))
    print(Hangrend("ares"))


if __name__ == "__main__":
    main()

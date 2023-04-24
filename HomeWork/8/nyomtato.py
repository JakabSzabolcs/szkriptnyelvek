#!/usr/bin/env python3

# Az alábbi függvény visszaadja a nyomtatni kívánt konkrét oldalakat. Pl.: 1,2,3,5-7,12,14-17 -> 1,2,3,5,6,7,12,14,15,16,17
def Nyomtatas():
    s = input("Adja meg a nyomtatni kívánt oldalakat: ")
    s = s.split(",")
    result = []
    for i in s:
        if "-" in i:
            i = i.split("-")
            for j in range(int(i[0]), int(i[1])+1):
                result.append(str(j))
        else:
            result.append(i)
    return ",".join(result)


# A main programrészben meghívjuk a függvényt és kiíratjuk a visszatérési értékét.
def main():
    print(Nyomtatas())


if __name__ == "__main__":
    main()

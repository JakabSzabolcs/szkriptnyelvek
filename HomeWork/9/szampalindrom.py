#!/usr/bin/env python3


# A függvény eldönti, hogy a szám palindrom-e vagy sem.
def Palindrom(szam):
    szam = str(szam)
    for i in range(len(szam)//2):
        if szam[i] != szam[-i-1]:
            return False
    return True


# Ez a függvény eldönti, hogy az input prím-e vagy sem.
def Primszam(szam):
    if szam < 2:
        return False
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True


# Ez a függvény megkeresi a legkisebb prímszámot, ami nagyobb, mint az input és palindrom is.
def Fuggveny(N):
    M = N
    while True:
        if Primszam(M) and Palindrom(M):
            print(M)
            break
        M += 1


# A main programrészben meghívjuk a függvényt és kiíratjuk a visszatérési értékét.
def main():
    N = int(input("Adjon meg egy számot: "))
    Fuggveny(N)


if __name__ == "__main__":
    main()

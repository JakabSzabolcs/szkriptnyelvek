#!/usr/bin/env python3


def Palindrom(szam):
    szam = str(szam)
    for i in range(len(szam)//2):
        if szam[i] != szam[-i-1]:
            return False
    return True


def Primszam(szam):
    if szam < 2:
        return False
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True


def Fuggveny(N):
    M = N
    while True:
        if Primszam(M) and Palindrom(M):
            print(M)
            break
        M += 1


def main():
    N = int(input("Adjon meg egy számot: "))
    Fuggveny(N)


if __name__ == "__main__":
    main()

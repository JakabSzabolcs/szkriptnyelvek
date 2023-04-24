#!/usr/bin/env python3


def Palindrom(szam):
    szam = str(szam)
    for i in range(len(szam)//2):
        if szam[i] != szam[-i-1]:
            return False
    return True


def Fuggveny(N):
    result = 0
    for i in range(1, N):
        if Palindrom(i) and Palindrom(bin(i)[2:]):
            result += i
    return result


def main():
    print(Fuggveny(1000000))


if __name__ == "__main__":
    main()

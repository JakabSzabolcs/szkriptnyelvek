#!/usr/bin/env python3


def main():
    osszeg = 0
    for i in range(1, 101):
        osszeg += i
    print('A szamok osszege 1-tol 100-ig:', osszeg)

    osszeg = 0

    for i in range(1, 101):
        for j in str(i):
            osszeg += int(j)
    print('A szamok szamjegyeinek osszege 1-tol 100-ig:', osszeg)


if __name__ == "__main__":
    main()

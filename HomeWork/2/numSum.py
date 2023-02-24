#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#A) változat
def numSum(a, b):
    return a + b

if __name__ == '__main__':

#   A) változat

    if len(sys.argv) < 3:
        print("Nem adtál meg elég paramétert!")
    else:
        print(numSum(int(sys.argv[1]), int(sys.argv[2])))


#   B) változat

    a = int(input("Kérem az első számot: "))
    b = int(input("Kérem a második számot: "))
    print(numSum(a + b))

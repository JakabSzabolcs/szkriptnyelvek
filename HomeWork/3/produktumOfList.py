#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def produktumOfList(list):
    produktum = 1
    for i in list:
        produktum *= i
    return produktum


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    print(produktumOfList(l1))
    l2 = []
    print(produktumOfList(l2))

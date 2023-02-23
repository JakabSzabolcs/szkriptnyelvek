#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Inputról kér egy stringet, majd a string minden második karakterét nagybetűssé alakítja.

def SecondUpper(string):
    for i in range(len(string)):
        if i % 2 == 0:
            string[i] = string[i].upper()
    return ''.join(string)


if __name__ == '__main__':
    string = input('Give me a string: ')
    print(SecondUpper(list(string)))

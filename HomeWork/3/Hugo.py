#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def clearString(s):
    s = s.replace(" ", "")
    return s


if __name__ == '__main__':
    print(clearString("alma korte"))
    print(clearString("valami   szoveg"))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# decode, where "K = M, O = Q, E = G"
def decode(s):
    s = s.upper()
    return s.translate(str.maketrans("KOE", "MQG"))


if __name__ == '__main__':
    message = """"Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""
    print(decode(message))

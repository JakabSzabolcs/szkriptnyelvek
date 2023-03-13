#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decode(s):
    result = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - ord('A') + 2) % 26 + ord('A'))
            else:
                result += chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
        else:
            result += c
    return result


if __name__ == '__main__':
    message = """"Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""
    print(decode(message))

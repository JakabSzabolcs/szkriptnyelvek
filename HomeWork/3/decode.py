#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decode(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[alphabet[i]] = alphabet[(i + 2) % 26]

    decoded = ""
    for i in s:
        if i in dictionary:
            decoded += dictionary[i]
        else:
            decoded += i
    return decoded


if __name__ == '__main__':
    message = """"cbcq dgyk!

dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y nwrfml npmepykmxyqg lwcjtcr!

aqmimjjyi:

ynyb"""
    print(decode(message))

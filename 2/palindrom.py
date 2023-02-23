#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def palindrome(stringA, stringB):

    # Check if the strings have a common char, if not return -1
    if not set(stringA) & set(stringB):
        return -1

    # Strings to sorted lists
    listA = list(stringA)
    listB = list(stringB)

    # Lists of all substrings from the strings
    subA = [stringA[i:j] for i in range(len(stringA))
            for j in range(i + 1, len(stringA) + 1)]
    subB = [stringB[i:j] for i in range(len(stringB))
            for j in range(i + 1, len(stringB) + 1)]

    print(listA)
    print(listB)

    print(subA)
    print(subB)


if __name__ == '__main__':
    print(palindrome('abc', 'def'))
    print(palindrome('bac', 'bac'))
    print(palindrome('jdfh', 'fds'))


# bca   fac

# 2 common -> minda a ketto common char bele mehet a vegleges stringbe


#   bca -->   b c a  bc ca  bca


#  ['b', 'ba', 'bac', 'a', 'ac', 'c']       -        ['b', 'ba', 'bac', 'a', 'ac', 'c']


# 1>3
# 2>5
# 3>7

##!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Az alábbi fv eldönti, hogy egy string palindrom-e.

def palindrome(string):
    # String to list
    list = [char for char in string]
    # List to reversed list
    reversedList = list[::-1]
    # Compare the lists
    if list == reversedList:
        return True
    else:
        return False


if __name__ == '__main__':
    print(palindrome('indulagörögaludni'))
    print(palindrome('indulagörögaludn'))
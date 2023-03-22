#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


def palindrome2(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome2(s[1:-1])


if __name__ == '__main__':
    print(palindrome('alma'))
    print(palindrome('kajak'))
    print(palindrome2('alma'))
    print(palindrome2('kajak'))

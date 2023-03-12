import sys
import random as r

UPTO = 100
import sys
import random as r

UPTO = 100


def main():
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
    if i%100==0:
        print()
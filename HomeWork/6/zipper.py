#!/usr/bin/env python3

def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('z') + 1))

    for t in zip(chars, codes):
        print(t)
    print()
    #range-el
    for t in zip(chars, range(ord('a'), ord('z') + 1)):
        print(t)

if __name__ == "__main__":
    main()
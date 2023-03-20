#!/usr/bin/env python3


def main():
    f = open("text.txt", "r")
    for line in f:
        print(line, end="")


if __name__ == "__main__":
    main()

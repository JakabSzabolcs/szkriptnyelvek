#!/usr/bin/env python3
# encoding: utf-8


def main():
    file = open("string1.py", "r")
    file2 = open("string1_clean.py", "w")
    for line in file:
        if line[0] != "#" and line[1] != "!":
            file2.write(line)
    file.close()
    file2.close()


if __name__ == "__main__":
    main()

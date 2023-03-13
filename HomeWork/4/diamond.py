#!/usr/bin/env python3


def Diamond(height):
    for i in range(1, height+1):
        if i <= height/2:
            print(" " * (int(height/2)-i+1) + "*" * (2*i-1))
        else:
            print(" " * (i-int(height/2)-1) + "*" * (2*(height-i)+1))


def main():
    Diamond(11)


if __name__ == "__main__":
    main()

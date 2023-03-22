#!/usr/bin/env python3


def main():
    # f = open("valami.txt", "r")
    # for line in f:
    #     print(line.rstrip('\n'))

    # # vagy így is lehet:

    # sorok = f.readlines()
    # print(sorok)

    # f.close()

    # list comprehension-nel:
    sorok = [line.rstrip('\n') for line in open("valami.txt", "r")]
    print(sorok)


if __name__ == "__main__":
    main()

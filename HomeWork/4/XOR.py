#!/usr/bin/env python3


def XOR(a, b):
    if a and b:
        return False
    elif a or b:
        return True
    else:
        return False


def main():
    print(XOR(True, False))
    print(XOR(False, True))
    print(XOR(True, True))
    print(XOR(False, False))
    str1 = "python"
    str2 = None
    print(XOR(str1, str2))


if __name__ == "__main__":
    main()

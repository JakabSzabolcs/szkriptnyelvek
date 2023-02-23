#!/usr/bin/env python3

import socketserver
import http.server
import sys


def main():
    if sys.argv[1] == "Batman" or "Robin":
        print("Denevér veszély!")
    else:
        print("Hello " + sys.argv[1] + "!")


if __name__ == "__main__":
    main()

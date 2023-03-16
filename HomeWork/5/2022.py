#!/usr/bin/env python3

def distance(chara, charb):
    return str(abs(ord(chara) - ord(charb)))

def main():
    ketezerhuszonketto = (distance('a', 'c') +  distance('a', 'a') + distance('a', 'c') +distance('a', 'c') )
    print(ketezerhuszonketto)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

def Koszones(nev, koszones='Szia', vegjel='!'):
    """A függvény kiírja a képernyőre a köszöntést
    A köszönés alapértelmezett értéke 'Szia'
    A köszönés végére az alapértelmezett jel: '!'"""
    print(f"{koszones} {nev}{vegjel}")


def main():
    Koszones('Szabi')
    Koszones('Szabi', 'Na csá')
    Koszones('Szabi', 'Na csá', '!!!')


if __name__ == "__main__":
    main()

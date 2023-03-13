#!/usr/bin/env python3

def main():
    gyumolcsok = ["alma", "körte", "szilva", "barack", "narancs", "szőlő"]
    for gyumi in gyumolcsok:
        if gyumi == "barack":
            continue

        if gyumi == "szőlő":
            break

        print(gyumi)


if __name__ == "__main__":
    main()

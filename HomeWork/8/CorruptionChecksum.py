#!/usr/bin/env python3


def main():
    file = open("./tabla.txt", "r")
    sum = 0
    for line in file:
        numbers = line.split()
        numbers = list(map(int, numbers))
        sum += max(numbers) - min(numbers)
    print(sum)
    file.close()


if __name__ == "__main__":
    main()
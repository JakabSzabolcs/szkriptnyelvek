#!/usr/bin/env python3


def SumOfSameNumbers(numbers):
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i + 1) % len(numbers)]:
            sum += int(numbers[i])
    return sum

def main():
    if SumOfSameNumbers("1122") == 3:
        print("OK")
    if SumOfSameNumbers("1111") == 4:
        print("OK")
    if SumOfSameNumbers("1234") == 0:
        print("OK")
    if SumOfSameNumbers("91212129") == 9:
        print("OK")


if __name__ == "__main__":
    main()

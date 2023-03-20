#!/usr/bin/env python3


def print_board(board):
    print("+-----------------+")
    for i in range(8):
        print("|", end="")
        for j in range(8):
            if board[j] == i:
                print(" Q", end="")
            else:
                print(" .", end="")
        print(" |")
    print("+-----------------+")


def main():
    print_board([7, 3, 0, 2, 5, 1, 6, 4])
    print_board([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == "__main__":
    main()

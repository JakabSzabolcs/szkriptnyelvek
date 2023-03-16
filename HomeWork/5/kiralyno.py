#A feladat most csak annyi lesz, hogy egy lehetséges állást jelenítsünk meg "grafikusan". A sakktáblát mátrix helyett egy tömbben (listában) reprezentáljuk, pl.: [7,3,0,2,5,1,6,4]. Ennek jelentése: az 1. oszlopban a királynő alulról a 8. sorban van, a 2. oszlopban alulról a 4. sorban, stb. (A listában a sorok indexelése 0-tól indul.) Ebből a listából a következő sakktáblát lehetne megjeleníteni:
#
#+-----------------+
#| Q . . . . . . . |
#| . . . . . . Q . |
#| . . . . Q . . . |
#| . . . . . . . Q |
#| . Q . . . . . . |
#| . . . Q . . . . |
#| . . . . . Q . . |
#| . . Q . . . . . |
#+-----------------+


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
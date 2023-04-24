#!/usr/bin/env python3


def Nyomtatas():
    s = input("Adja meg a nyomtatni kívánt oldalakat: ")
    s = s.split(",")
    result = []
    for i in s:
        if "-" in i:
            i = i.split("-")
            for j in range(int(i[0]), int(i[1])+1):
                result.append(str(j))
        else:
            result.append(i)
    return ",".join(result)


def main():
    print(Nyomtatas())


if __name__ == "__main__":
    main()

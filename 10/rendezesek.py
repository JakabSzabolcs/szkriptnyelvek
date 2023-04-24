#!/usr/bin/env python3


def LastChar(s):
    return s[-1]


def get_id(s):
    return s.split(":")[0]


def main():

    # ELSO FELADAT
    data = [
        (1, 'Albany', 'NY', 162692),
        (3, 'Allegany', 'NY', 11986),
        (121, 'Wyoming', 'NY', 8722),
        (123, 'Yates', 'NY', 5094)
    ]
    print(sorted(data, key=LastChar))
    print("-"*20)

    # MASODIK FELADAT
    users = ['10:User1', '80:User2', '100:User3',
             '00:User4', '75:User4', '45:User5']
    print(sorted(users, key=get_id))
    print("-"*20)

    # HARMADIK FELADAT
    li = [[2, 6], [1, 3], [5, 4]]
    print(sorted(li, key=lambda x: x[1]))
    print("-"*20)


if __name__ == "__main__":
    main()

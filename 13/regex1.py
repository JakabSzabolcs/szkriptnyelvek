
import re


def find(keresett, s):
    m = re.search(keresett, s)
    if m:
        print("Találat: ", m.group())
        print("Kezdete: ", m.start())
        print("Vége: ", m.end())
        print("Kezdete és vége: ", m.span())
    else:
        print("Nincs találat!")


def main():
    s = "Reguláris kifejezés"
    keresett = "kif"
    m = re.search(keresett, s)
    print(m)
    print(m.group())
    print(m.span())
    find(keresett, s)

    m2 = re.search("cica", s)
    print(m2)
    if m2:
        print(m2.group())



if __name__ == "__main__":
    main()


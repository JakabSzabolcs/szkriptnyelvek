#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.verem = []

    def __str__(self):
        return str(self.verem)

    def betesz(self, elem):
        self.verem.append(elem)

    def kivesz(self):
        if self.ures():
            return None
        else:
            return self.verem.pop()

    def meret(self):
        return len(self.verem)

    def ures(self):
        return self.meret() == 0



class Sor(Verem):
    def __init__(self):
        super().__init__()

    def betesz(self, elem):
        self.verem.insert(0, elem)

    def kivesz(self):
        if self.ures():
            return None
        else:
            return self.verem.pop()

    def __str__(self):
        return str(self.verem[::-1])



def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

    print("*" * 20)

    s = Sor()
    print(s)
    print(s.ures())
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)
    print(s.meret())
    print(s.ures())
    x = s.kivesz()
    print(x)
    print(s)
    s.kivesz()
    s.kivesz()
    x = s.kivesz()
    print(x)


if __name__ == '__main__':
    main()
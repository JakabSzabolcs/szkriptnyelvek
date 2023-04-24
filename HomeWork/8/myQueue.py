#!/usr/bin/env python3


class MyQueue:
    def __init__(self):
        self.verem1 = []
        self.verem2 = []
        self.meret = 0

    def append(self, elem):
        self.verem1.append(elem)
        self.meret += 1

    def popleft(self):
        if self.meret == 0:
            return None
        else:
            for i in range(self.meret):
                self.verem2.append(self.verem1.pop())
            x = self.verem2.pop()
            for i in range(self.meret - 1):
                self.verem1.append(self.verem2.pop())
            self.meret -= 1
            return x

    def is_empty(self):
        return True if self.meret == 0 else False

    def size(self):
        return self.meret


def main():
    q = MyQueue()
    print(q.is_empty())  # True
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.is_empty())  # False
    print(q.size())      # 3
    print(q.popleft())   # 1
    print(q.popleft())   # 2
    print(q.popleft())   # 3
    print(q.popleft())   # None


if __name__ == "__main__":
    main()
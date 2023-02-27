#!/usr/bin/env python3


# d = [1,2,3]
# ennek egy másolatát úgy hozzuk létre hogy e = d[:] vagy van copy() metódusa mivel a lista is egy objektum
# a másolatban a változások nem befolyásolják az eredeti listát

# .append(element) metódus hozzáad egy elemet a listához
# .pop(index) metódus eltávolítja a megadott indexű elemet a listából és visszaadja azt, ha nincs megadva index akkor az utolsót
# .remove(element) metódus eltávolítja a megadott elemet a listából
# .insert(index, element) metódus beszúr egy elemet a megadott index helyére
# .index(element) metódus visszaadja az elem indexét a listában
# .count(element) metódus visszaadja az elem előfordulásainak számát a listában
# .sort() metódus rendez egy listát
# .reverse() metódus megfordítja a listát
# .clear() metódus törli a listát
# .copy() metódus másolatot készít a listáról
# .extend(list) metódus hozzáad egy listát a listához

# deque: https://docs.python.org/3/library/collections.html#collections.deque
# help()
# help(list.append)
# all list methods: https://docs.python.org/3/tutorial/datastructures.html

# list comprehension
# [expression for item in list if conditional]
# [x*2 for x in range(10)]
# list comprehension with if else
# [x if x % 2 == 0 else x*2 for x in range(10)]
# list comprehension with nested loops
# [x*y for x in [1,2,3] for y in [3,1,4] if x != y]

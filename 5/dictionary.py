#!/usr/bin/env python3

# kulcs érték tárolására használjuk a dictionary-t
# a kulcsok egyediek

def main():
    empty_Dict = {}
    print(empty_Dict)
    animal_Dict = {"a": "alma",
                   "b": "banán",
                   "c": "citrom"}

    print(animal_Dict["a"])
    animal_Dict["d"] = "dinnye"
    print(animal_Dict.get('f'))  # none lesz, mert nincs ilyen kulcs
    print('f' in animal_Dict)  # False

    print(list(animal_Dict.keys()))  # kulcsok
    print(list(animal_Dict.values()))  # értékek
    # del
    del animal_Dict["a"]
    print(animal_Dict)


if __name__ == "__main__":
    main()

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


if __name__ == "__main__":
    main()

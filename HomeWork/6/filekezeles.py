

#open /2/string1.py delete all comments and save it to string1_clean.py to this folder


def main():
    f = open("string1.py", "r")
    lines = f.readlines()
    for line in lines:
        if line.startswith("#"):
            continue
        print(line, end="")
    f.close()

if __name__ == "__main__":
    main()

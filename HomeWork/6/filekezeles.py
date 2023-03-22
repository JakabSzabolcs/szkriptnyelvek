

#open string1.py delete all comments and save it to string1_clean.py to this folder

def main():
    file = open("string1.py", "r")
    file2 = open("string1_clean.py", "w")
    for line in file:
        if line[0] != "#":
            file2.write(line)
    file.close()
    file2.close()


if __name__ == "__main__":
    main()

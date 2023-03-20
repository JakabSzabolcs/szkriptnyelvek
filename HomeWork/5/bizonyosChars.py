#valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") where chars is a string of valid characters and optional
# print the text's characters that are in chars

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    for char in text:
        if char in chars:
            print(char, end="")
    print()


def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    main()
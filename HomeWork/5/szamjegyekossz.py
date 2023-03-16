#2^15 = 32768 és a számjegyek összege 3 + 2 + 7 + 6 + 8 = 26.
#
#Mennyi 2^1000 számjegyeinek az összege?



def main():
    print(sum([int(x) for x in str(2 ** 1000)]))


if __name__ == "__main__":
    main()

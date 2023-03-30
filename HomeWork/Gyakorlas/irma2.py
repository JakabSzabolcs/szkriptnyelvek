#plot a chart of y = e^x where x ]0,1[

import math


def main():
    x = 0.05
    while x < 1:
        print(x, math.exp(x))
        x += 0.05


if __name__ == "__main__":
    main()
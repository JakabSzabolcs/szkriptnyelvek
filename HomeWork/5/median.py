#Feladat: adott számoknak egy listája. Határozzuk meg a medián értékét.



def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def main():
    if median([1, 2, 3, 4, 5]) == 3:
        print('OK')
    if median([3, 1, 2, 5, 3]) == 3:
        print('OK')
    if median([1, 300, 2, 200, 1]) == 2:
        print('OK')
    if median([3, 6, 20, 99, 10, 15]) == 12.5:
        print('OK')

if __name__ == "__main__":
    main()
def main():
    camelCase = input("name of variable in camelCase ")
    snake(camelCase)


def snake(case):
    for letter in case:
        if letter.isupper():
            letter = letter.lower()
            print(f"_{letter}", end="")
        else:
            print(letter, end="")
    print("")


main()

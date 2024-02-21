def main():
    camelCase = input("name of variable in camelCase ")
    snake(camelCase)


def snake(case):
    for letter in case:
        print(letter, end=" ")


main()

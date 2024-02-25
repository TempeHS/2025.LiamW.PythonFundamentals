def main():
    tweet = input("Tweet: ")
    for letter in tweet:
        vowelreplace(letter)
    print("")


def vowelreplace(check):
    if check == "a" or check == "e" or check == "i" or check == "o" or check == "u":
        print("", end="")
    else:
        print(check, end="")


main()

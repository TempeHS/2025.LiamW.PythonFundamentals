def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number = len(s)
    # checks if too short or large
    if number < 2 or number > 6:
        return False
    elif not s.isalnum():
        return False
    # checks if all character uppercase
    elif not s.isupper():
        return False
    # checks if first two are letters
    elif not s[0].isalpha or not s[1].isalpha():
        return False
    # checks if number is not in middle
    elif number > 2 and not check(s[2:number]):
        return False
    else:
        return True


def check(t):
    foundnumber = False
    for letter in t:
        if letter.isnumeric():
            foundnumber = True
        elif foundnumber:
            return False
    return True


main()

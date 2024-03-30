import random


tries = 1


def main():
    lvl = get_level()
    try:
        n = 0
        wrong = 0
        while n < 10:
            x = generate_integer(lvl)
            y = generate_integer(lvl)
            n = n + 1
            tries = 1
            while tries <= 3:
                answer = input(f"{x} + {y} = ")
                answer = int(answer)
                if answer == x + y:
                    break
                else:
                    print("EEE")
                    tries = tries + 1
                    pass
            if tries == 3:
                wrong = wrong + 1
    except ValueError:
        pass
    print(f"{10-int(wrong)}/10")


def get_level():
    while True:
        try:
            number = input("Level: ")
            number = int(number)
            if number > 3 or number <= 0:
                pass
            else:
                return number
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        randint = random.randint(0, 9)
        return randint
    elif level == 2:
        randint = random.randint(10, 99)
        return randint
    elif level == 3:
        randint = random.randint(100, 999)
        return randint


if __name__ == "__main__":
    main()

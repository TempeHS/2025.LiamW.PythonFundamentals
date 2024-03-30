import random

n = 0
tries = 1


def main():
    lvl = get_level()
    try:
        while n < 10:
            x = generate_integer(lvl)
            y = generate_integer(lvl)
            n = n + 1
            answer = input(f"{x} + {y} = ")
            answer = int(answer)
            tries = 1
            while tries <= 3:
                if answer == x + y:
                    break
                else:
                    print("EEE")
                    pass
    except ValueError:
        pass


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
        randint = random.radint(10, 99)
        return randint
    elif level == 3:
        randint = random.radint(100, 999)
        return randint


if __name__ == "__main__":
    main()

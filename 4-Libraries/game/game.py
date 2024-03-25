import random

while True:
    try:
        n = int(input("Level: "))
        if n >= 1:
            break
    except ValueError:
        pass

number = random.randint(1, n)

while True:
    guess = input("Guess: ")
    if not guess.isnumeric():
        pass
    elif int(guess) < 0:
        pass
    elif int(guess) < number:
        print("Too small!")
    elif int(guess) > number:
        print("Too big!")
    else:
        print("Just right!")
        break

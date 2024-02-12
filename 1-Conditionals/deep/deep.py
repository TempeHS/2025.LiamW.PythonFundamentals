Answer = input("Answer, Great Question of Life, the Universe and Everything: ")
answer = Answer.strip().lower()
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

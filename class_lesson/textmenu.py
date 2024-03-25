import sys

menu = ["drinks", "foods", "snacks", "exit"]
items = []
n = 0
while True:
    while True:
        if n > 3:
            break
        print(f"{n + 1}. {menu[n]}")
        n = n + 1
    item = input("What would you like: ")
    if item == "4":
        sys.exit("Thanks for using menu")
    else:
        print(f"thank you for choosing item {item}")

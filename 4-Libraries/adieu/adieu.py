import inflect

p = inflect.engine()
n = 1
namelist = []
while True:
    try:
        namelist.append(input("Name: "))
    except EOFError:
        print("")
        break

print("Adieu, adieu, to ", end="")
for name in namelist:
    n = n + 1
    if len(namelist) == 1:
        print(f"{name}")
    elif n < len(namelist) + 1:
        print(f"{name}, ", end="")
    else:
        print(f"and {name}")

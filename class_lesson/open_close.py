# This increments the whole list by one
n = 0
strippedlist = []
with open("myText.txt", "r") as file:
    number = file.readlines()
for num in number:
    Number = number[n]
    Number = Number.removesuffix("\n")
    strippedlist.append(Number)
    n = n + 1
n = 0
file = open("myText.txt", "w")
for num in number:
    Number = number[n]
    Number = int(Number) + 1
    Number = str(Number)
    file.write(Number)
    file.write("\n")
    n = n + 1
file.close

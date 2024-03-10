List = {}

while True:
    try:
        item = input("What To Buy: ")
        if item in List:
            List[item] = List[item] + 1
        else:
            List[item] = 1
    except EOFError:
        print("")
        break
    except KeyError:
        pass

sortedlist = sorted((List))
for item in sortedlist:
    print(f"{List[item]} {item.upper()}")

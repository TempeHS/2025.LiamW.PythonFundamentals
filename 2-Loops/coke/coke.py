def main():
    remain = 50
    while remain > 0:
        amount = input("Insert Coin 10, 25 or 5! ")
        if amount == "25" or amount == "10" or amount == "5":
            amount = int(amount)
            remain = int(remain) - amount
            if remain > 0:
                print(f"Amount Due: {remain}")
        else:
            print(f"Amount Due: {remain}")
    if remain <= 0:
        remainder = str(remain).strip("-")
        print(f"Change Owed: {remainder}")


main()

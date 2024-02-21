def main():
    remain = 50
    while remain > 0:
        amount = input("Insert Coin 10, 25 or 5! ")
        if amount == "25" or "10" or "5":
            amount = int(amount)
            remain = int(remain) - amount
            print(f"Amount Due: {remain}")
    if remain <= 0:
        remainder = str(remain).strip("-")
        print(f"Change Owed: {remainder}")


main()

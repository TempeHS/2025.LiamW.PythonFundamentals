def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Get rid of dollar and Return as float
    D = d.lstrip("$").removesuffix("0")
    return float(D)


def percent_to_float(p):
    # get rid of % and Return as float
    P = float(p.removesuffix("%")) / 100
    return P


main()

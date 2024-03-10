months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def main():
    while True:
        date = input("What's The Date? ")
        try:
            if date.find("/") > -1:
                month, day, year = date.split(sep="/")
                if valid(month, day):
                    break
            elif date.find(",") > -1:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                month = months[month]
                if valid(month, day):
                    break
        except KeyError or ValueError:
            pass
    print(f"{year}-{int(month):02}-{int(day):02}")


def valid(mon, day):
    if int(mon) > 12:
        return False
    elif int(day) > 31:
        return False
    else:
        return True


main()

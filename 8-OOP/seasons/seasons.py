from datetime import date
from datetime import timedelta
import sys
import inflect

p = inflect.engine()


class DOB:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    @classmethod
    def min(self):
        timedelta()

    def __str__(self):
        print(f"{self.year}-{self.month}-{self.day}")


def main():
    try:
        # User Bday
        DoB = input("What's your date of birth: ")
        Birth = clconvert(DoB)
        Bday = date(Birth.year, Birth.month, Birth.day)
        # Today
        DoT = date.today()
        DoT = clconvert(str(DoT))
        DoT = date(DoT.year, DoT.month, DoT.day)
        # Difference
        diff = DoT - Bday
        days, _ = str(diff).split(",")
        days = days.strip(" days")
        mins = int(days) * 24 * 60
        print(p.number_to_words(mins))
    except ValueError:
        sys.exit("Invalid Value/Format")


def clconvert(date):
    YYYY, MM, DD = date.split("-")
    return DOB(YYYY, MM, DD)


if __name__ == "__main__":
    main()

def main():
    intime = input("What's the time ")
    Time = float(convert(intime))
    if 7 <= Time <= 8:
        print("breakfast time")
    elif 12 <= Time <= 13:
        print("lunch time")
    elif 18 <= Time <= 19:
        print("dinner time")
    else:
        print("nothing")


def convert(time):
    hr, min = time.split(":")
    return float(hr) + float(min) / 60


main()


# if __name__ == "__main__":

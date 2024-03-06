while True:
    top, bot = input("Fraction of fuel left: ").split(sep="/")
    try:
        top = int(top)
        bot = int(bot)
        top / bot
        if top > bot:
            top = "failure"
            int(top)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
top = int(top)
bot = int(bot)
percentage = round((top / bot) * 100)
if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")

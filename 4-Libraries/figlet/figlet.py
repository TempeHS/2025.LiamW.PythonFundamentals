from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    """
    randomfont = random.choice(figlet.getFonts())
    message = input("What's the message? ")
    print(figlet.renderText(message))
    """
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            message = input("What's the message? ")
            Font = sys.argv[2]
            figlet.setFont(font=Font)
            print(figlet.renderText(message))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

import sys
import requests

try:
    amount = sys.argv[1]
    amount = float(amount)
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    res = res.json()
    notprice = res["bpi"]
    notprice = notprice["USD"]
    price = float(notprice["rate"].replace(",", ""))
    print(f"{(price * amount):,.4f}")
except requests.RequestException:
    sys.exit()
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

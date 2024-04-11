import csv
import sys
from tabulate import tabulate

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    with open(sys.argv[1], "r") as file:
        info = csv.reader(file)
        print(tabulate(info))
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

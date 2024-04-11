import sys

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines:
            linestripped = line.strip()
            if line.startswith(""):
                lines.remove(line)
            elif line.startswith("#"):
                lines.remove(line)
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

print(len(lines))

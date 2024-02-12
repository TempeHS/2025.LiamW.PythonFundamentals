equation = input("give an equation: ")
x, y, z = equation.split()

if y == "+":
    sum = int(x) + int(z)
    print(float(sum))
elif y == "-":
    diff = int(x) - int(z)
    print(float(diff))
elif y == "*":
    product = int(x) * int(z)
    print(float(product))
elif y == "/":
    quotient = int(x) / int(z)
    print(float(quotient))

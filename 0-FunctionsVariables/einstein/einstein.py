def main():
    mass = int(input("How Heavy in Kg: "))
    print(einstein(mass))


def einstein(to):
    energy = to * 300000000 * 300000000
    return int(energy)


main()

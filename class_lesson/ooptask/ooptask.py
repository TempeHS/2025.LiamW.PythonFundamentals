class Shape:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return self.__name__


class Cube(Shape):
    def __init__(self, colour, x, y, z, length):
        super().__init__(colour, x, y, z)
        self.length = length

    def __str__(self):
        return super().__str__()

    def Volume(self):
        Vol = self.length**3
        return Vol

    def SA(self):
        face = self.length**2
        SurfaceA = face * 6
        return SurfaceA

    def crossSec(self):
        face = self.length**2
        return face


def main():
    cube = Cube("blue", 0, 0, 0, 3)
    print(cube.Volume())


if __name__ == "__main__":
    main()

class Shape:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return self.__name__

    def getlocation(self):
        return f"({self.x},{self.y},{self.z})"

    def setlocation(self): ...
    def getcolour(self): ...


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


class Sphere(Shape):
    def __init__(self, colour, x, y, z, radius):
        super().__init__(colour, x, y, z)
        self.radius = radius

    def __str__(self):
        return super().__str__()

    def Volume(self):
        Vol = (4 / 3) * 3.14 * (self.radius**3)
        return Vol

    def SA(self):
        SurfaceA = 4 * 3.14 * (self.radius**2)
        return SurfaceA

    def crossSec(self):
        face = 3.14 * (self.radius**2)
        return face


def main():
    cube = Cube("blue", 0, 0, 0, 3)
    print(cube.getlocation())
    print(cube.Volume())


if __name__ == "__main__":
    main()

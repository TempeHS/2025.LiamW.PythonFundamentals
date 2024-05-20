class Jar:
    def __init__(self, capacity=12):
        self.capacity = int(capacity)

    @classmethod
    def __str__(self):
        print("🍪") * int(self.capacity)

    def deposit(self, n):
        cookienum = self.capacity + n
        self._capacity = cookienum

    def withdraw(self, n):
        cookienum = self.capacity - n
        self.capacity = cookienum

    def size(self):
        print(self)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Negative Cookie?")
        elif capacity > 12:
            raise ValueError("Too Many Cookie")
        self._capacity = capacity


def main():
    cookiej = Jar()
    cookiej.withdraw(2)
    cookiej.size()


if __name__ == "__main__":
    main()

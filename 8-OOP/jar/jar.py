class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    @classmethod
    def __str__(self):
        n = 0
        list = []
        times = self.capacity
        while n < times:
            list.append("🍪")
            n = n + 1
        return list

    def deposit(self, n):
        cookienum = self.capacity + n
        self._capacity = cookienum

    def withdraw(self, n):
        cookienum = self.capacity - n
        self.capacity = cookienum

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

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not size == self.capacity:
            return ValueError
        self._size = size


def main():
    cookiej = Jar()
    cookiej.withdraw(2)
    cookiej.size()


if __name__ == "__main__":
    main()

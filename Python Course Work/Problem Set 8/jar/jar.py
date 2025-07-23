class Jar:
    def __init__(self, capacity=12):
        size = 0
        self.capacity = capacity
        self.size = size

    def __str__(self):
        
        cookies = ['🍪'] * self.size
        return "".join(cookies)

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError

        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError

        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError

        else:
            self._size = size


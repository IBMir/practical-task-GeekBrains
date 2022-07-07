class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def find_the_mass(self):
        return self._width * self._length * 25 * 5


if __name__ == '__main__':
    weight = Road(20, 5000)
    print(weight.find_the_mass())

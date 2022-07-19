class Clothing_manufacturing:
    def __init__(self, size, height):
        self.__size = size
        self.__height = height

    def coat_fabric_consumption(self, quantity=1):
        return round((self.__size / 6.5 + 0.5) * quantity)

    def suit_fabric_consumption(self, quantity=1):
        return round((2 * self.__height + 0.3) * quantity)

    def total_fabric_consumption(self):
        return self.coat_fabric_consumption() + self.suit_fabric_consumption()


if __name__ == '__main__':
    procurement1 = Clothing_manufacturing(48, 170)
    print(procurement1.coat_fabric_consumption())
    print(procurement1.suit_fabric_consumption())
    print(procurement1.total_fabric_consumption())
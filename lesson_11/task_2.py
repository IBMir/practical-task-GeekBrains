class Division:
    def __init__(self, divisible=(int, float), divisor=(int, float)):
        self.divisible = divisible
        self.divisor = divisor

    def division(self):
        try:
            return self.divisible / self.divisor
        except ZeroDivisionError:
            return 'Деление на ноль не допустимо.'


if __name__ == '__main__':
    f = Division(12, 0)
    print(f.division())

class Cell:
    def __init__(self, number_of_cells):
        if isinstance(number_of_cells, int):
            self.number_of_cells = number_of_cells
        else:
            raise ValueError('Количество ячеек клетки только целое число.')

    def __add__(self, other):
        return self.number_of_cells + other.number_of_cells

    def __sub__(self, other):
        if (self.number_of_cells - other.number_of_cells) < 0:
            return 'Разность количества ячеек двух клеток должна быть больше нуля.'
        else:
            return self.number_of_cells - other.number_of_cells

    def __mul__(self, other):
        return self.number_of_cells * other.number_of_cells

    def make_order(self, row):
        return (('*' * row) + '\n') * (self.number_of_cells // row) + '*' * (self.number_of_cells % row)


if __name__ == '__main__':
    a = Cell(10)
    b = Cell(15)
    print(a + b)
    print(b - a)
    print(a * b)
    print(a.make_order(4))

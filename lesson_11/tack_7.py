class Complex_numbers:
    def __init__(self, material, imaginary):
        self.material = material
        self.imaginary = imaginary

    def __add__(self, other):
        mat = self.material + other.material
        im = self.imaginary + other.imaginary
        return self.output(mat, im)

    def __mul__(self, other):
        mat = (self.material * other.material) + (self.imaginary * other.imaginary) * -1
        im = (self.material * other.imaginary) + (self.imaginary * other.material)
        return self.output(mat, im)

    def output(self, material, imaginary):
        if material != 0:
            if imaginary > 0:
                return f'{material}+{imaginary}i'
            elif imaginary == 0:
                return f'{material}'
            else:
                return f'{material}{imaginary}i'
        else:
            if material == 0 and imaginary == 0:
                return 0
            else:
                return f'{imaginary}i'


if __name__ == '__main__':
    n1 = Complex_numbers(1, 3)
    n2 = Complex_numbers(2, 1)
    print(n1 + n2)
    print(n1 * n2)

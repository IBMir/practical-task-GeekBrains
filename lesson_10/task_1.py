class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.data_verification()

    def data_verification(self):
        if isinstance(self.list_of_lists, list):
            for i in self.list_of_lists:
                if isinstance(i, list):
                    pass
                else:
                    raise ValueError('Принимает только список списков.')
        else:
            raise ValueError('Принимает только список списков.')

    def __str__(self):
        mart = ''
        for i in self.list_of_lists:
            for y in i:
                mart += str(y) + ' '
            mart += '\n'
        return mart

    def __add__(self, other):
        for i in range(len(self.list_of_lists)):
            for y in range(len(self.list_of_lists[i])):
                self.list_of_lists[i][y] += other.list_of_lists[i][y]
        return self.__str__()




if __name__ == '__main__':
    l = [[23, 4, 5], [1414, 43, 2], [0, 7, 6], [454, 1, 22], [111, 21, 1]]
    k = [[3, 2, -565], [2, 343, 1], [4, 0, 12], [-2, -9797, 21], [511, 331, 0]]
    f = Matrix(l)
    f2 = Matrix(k)
    print(f)
    print(f2)
    f += f2
    print(f)
    print(f2)
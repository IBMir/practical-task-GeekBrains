import re


class Data:
    def __init__(self, d_m_y):
        self.valid(d_m_y)
        self.d_m_y = Data.in_the_number(d_m_y)

    @staticmethod
    def valid(line):
        if re.match(r'(([0-3]\d)|[1-9])-(([0-2]\d)|[1-9]|31)-\d+', line) == None:
            raise ValueError('Принимает дату в виде строки формата «день-месяц-год»')

    @classmethod
    def in_the_number(cls, line):
        line = list(map(int, line.split('-')))
        return f'{line[0]}-{line[1]}-{line[2]}'


if __name__ == '__main__':
    v = Data('19-7-2020')
    print(v.d_m_y)

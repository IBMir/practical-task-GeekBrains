class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._salary = {
            'директор': {"wage": 245000, "bonus": 85000},
            'бухгалтер': {"wage": 85000, "bonus": 35000},
            'сисадмин': {"wage": 45000, "bonus": 15000},
            'сварщик': {"wage": 55000, "bonus": 19000},
            'повар': {"wage": 35000, "bonus": 10000},
        }


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'{str(self.name).title()} {str(self.surname).title()}'

    def get_total_income(self):
        if self.position in self._salary:
            return f'Доход сотрудника {str(self.name).title()} {str(self.surname).title()},в должности {self.position} составляет {self._salary[self.position]["wage"] + self._salary[self.position]["bonus"]} рублей.'
        else:
            return 'Такой должности у нас нет.'


if __name__ == '__main__':
    employee = Position('иван', 'иванов', 'директор')
    print(employee.get_full_name())
    print(employee.get_total_income())

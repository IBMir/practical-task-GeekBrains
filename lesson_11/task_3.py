class List_of_numbers:
    result = []

    def __init__(self):
        data = input('Введите число и нажмите Enter - ')
        self.exc(data)



    def exc(self, data):
        while data != 'stop':
            try:
                self.result.append(int(data))
                data = input('Введите число и нажмите Enter (для завершения введите: stop) - ')
            except ValueError:
                print('Введенные вами данные не являются числом')
                data = input('Введите число и нажмите Enter (для завершения введите: stop) - ')
        print(self.result)


if __name__ == '__main__':
    r = List_of_numbers()

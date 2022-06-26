def type_logger(function):
    def wrapper(*args):
        arguments = dict()
        for i in args:
            arguments[i] = type(i)
        return f'{str(function).split()[1]} {arguments}'
    return wrapper


@type_logger
def calc_cube(x, y):
    return x * y


if __name__ == '__main__':
    print(calc_cube(5, 2))

def sum_of_digits(numder):
    list_number = [int(i) for i in str(numder)]
    return sum(list_number)


if __name__ == '__main__':
    initial_list = [i ** 3 for i in range(1, 1001) if i % 2 != 0]
    divided_by_7 = [i for i in initial_list if sum_of_digits(i) % 7 == 0]
    print(sum(divided_by_7))
    initial_list_17 = [(i ** 3) + 17 for i in range(1, 1001) if i % 2 != 0]
    divided_by_7 = [i for i in initial_list_17 if sum_of_digits(i) % 7 == 0]
    print(sum(divided_by_7))

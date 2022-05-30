for i in range(1, 101):
    if 5 <= i % 10 <= 9 or i % 10 == 0 or 11 <= i <= 14:
        print(i, 'процентов')
    elif 2 <= i % 10 <= 4:
        print(i, 'процента')
    else:
        print(i, 'процент')

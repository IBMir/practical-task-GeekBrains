from sys import argv

with open('sales.txt', 'a', encoding='utf-8') as f:
    try:
        f.writelines(argv[1])
        f.writelines('\n')
    except IndexError:
        print('Некорректно указана сумма продаж булочной.')

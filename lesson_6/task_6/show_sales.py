from sys import argv

with open('sales.txt', 'r', encoding='utf-8') as f:
    try:
        recordings = (i for i in f)
        if len(argv) == 2:
            try:
                for i in range(int(argv[1])):
                    print(next(recordings).replace('\n', ''))
            except StopIteration:
                print('Список выведен польностью.')
        elif len(argv) == 3:
            try:
                for i in range(1, int(argv[2]) + 1):
                    if i >= int(argv[1]):
                        print(next(recordings).replace('\n', ''))
                    else:
                        next(recordings)
            except StopIteration:
                print('Список выведен польностью.')
        else:
            print('Некорректно указаны данные.')
    except IndexError:
        print('Некорректно указаны данные.')

def time(duration):
    if 0 < duration < 60:
        print(f'{duration % 60} сек.')
    elif 60 <= duration < 3600:
        print(f'{duration // 60} мин., {duration % 60} сек.')
    elif 3600 <= duration < 86400:
        print(f'{duration // 3600} час., {duration % 3600 // 60} мин., {duration % 60} сек.')
    elif 86400 <= duration:
        print(
            f'{duration // 86400} дн., {duration % 86400 // 3600} час., {duration % 3600 // 60} мин., {duration % 60} сек.')
    else:
        print('Запись не корректна')


if __name__ == '__main__':
    user_data = int(input('Укажите промежуток времени: '))
    time(user_data)

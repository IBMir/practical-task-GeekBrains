def price(number, cent='00'):
    if int((number - int(number)) * 100) == 0:
        return f'{int(number)} руб., {cent} коп.'
    else:
        return f'{int(number)} руб., {int((number - int(number)) * 100)} коп.'


prices = [57.8, 46.51, 97, 233, 43, 6.33, 4]
for i in sorted(prices):
    print(price(i))
print()
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
new_list = sorted(prices[:], reverse=True)
print(new_list)
print()
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
for i in new_list[0:5]:
    print(price(i))
def is_a_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = None
while i != lst[-1]:
    for i in lst:
        indx = lst.index(i)
        if is_a_number(i) and lst[indx - 1] != '"':
            if 0 < int(i) < 9 and '+' not in lst[indx]:
                lst[indx] = '0' + i
            elif -10 < int(i) < 10 and ('+' in lst[indx] or '-' in lst[indx]):
                lst[indx] = lst[indx][0] + '0' + lst[indx][1]
            lst.insert(indx, '"')
            lst.insert(indx + 2, '"')
print(lst)
for i in lst:
    if i != '"':
        print(i, end=' ')

result = dict()
with open('users.csv', 'r') as f:
    key = (i.replace('\n', '').replace(',', ' ') for i in f)
    with open('hobby.csv','r') as f:
        meaning = (i.replace(',\n', '').replace(',', ', ').replace('\n', '') for i in f)
        for k in key:
            try:
                result[k] = next(meaning)
            except StopIteration:
                result[k] = None
with open('site_users.txt', 'w', encoding='utf-8') as f:
    f.write(str(result))
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Ольга', 'Глеб'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for i in range(len(tutors)):
    try:
        print((tutors[i], klasses[i]))
    except IndexError:
        print((tutors[i], None))

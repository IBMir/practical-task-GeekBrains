def num_translate(number):
    dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    return dictionary.get(number)


if __name__ == '__main__':
    n = 1
    while n != '':
        n = input('Write the number - ')
        print(num_translate(n))

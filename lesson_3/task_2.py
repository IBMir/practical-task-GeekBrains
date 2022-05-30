def num_translate_adv(number):
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
    if 64 < ord(number[0]) < 91:
        return str(dictionary.get(number.lower())).title()
    else:
        return dictionary.get(number)


if __name__ == '__main__':
    while True:
        n = input('Write the number - ')
        if n == '':
            break
        else:
            print(num_translate_adv(n))

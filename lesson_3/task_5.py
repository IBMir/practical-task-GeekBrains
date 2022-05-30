from random import choices


def get_jokes(qantiti, *lists):
    jokes = []
    for j in range(qantiti):
        joke = ''
        for i in lists:
            joke += choices(i)[0] + ' '
        jokes.append(joke)
    return jokes



if __name__ == '__main__':
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    print(get_jokes(5, nouns, adverbs, adjectives))

from task_3 import thesaurus


def thesaurus_adv(*name):
    s = {}
    for i in name:
        key_last_name = i.split()[1][0]
        if key_last_name not in s:
            s[key_last_name] = thesaurus(i, s={})
        else:
            s[key_last_name] = thesaurus(i, s=s[key_last_name])
    sorted_s = dict(sorted(s.items(), key=lambda x: x[0]))
    return sorted_s


if __name__ == '__main__':
    print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

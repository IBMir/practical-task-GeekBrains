def thesaurus(*name, s={}):
    for i in name:
        if i[0] in s:
            s[i[0]].append(i)
        else:
            s[i[0]] = []
            s[i[0]].append(i)
    sorted_s = dict(sorted(s.items(), key=lambda x: x[0]))
    return sorted_s


if __name__ == '__main__':
    print(thesaurus("Иван", "Мария", "Петр", "Илья"))

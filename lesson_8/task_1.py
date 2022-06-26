import re


def email_parse(email):
    dictionary = {'username': None, 'domain': None}
    try:
        email = re.findall(r'^(\w+)@(\w+\.\w{2}$)', email)[0]
    except IndexError as i:
        return f'''raise ValueError(msg)
ValueError: wrong email: {email}'''
    dictionary['username'] = email[0]
    dictionary['domain'] = email[1]
    return dictionary


if __name__ == '__main__':
    email = input('Введите ваш email адрес: ')
    print(email_parse(email))

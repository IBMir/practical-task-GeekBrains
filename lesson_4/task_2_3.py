import requests
from pprint import pprint
from datetime import datetime


def currency_rates(currency):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    if currency.upper() in response['Valute']:
        date = datetime.strptime(response['Date'][:10], "%Y-%m-%d")
        name = response['Valute'][currency.upper()]['Name']
        rate = response['Valute'][currency.upper()]['Value']
        return f'''Центральный банк Российской Федерации установил с {date.strftime('%d %m %Y')} следующий курс:
        1 {name} - {rate} рубля Российской Федерации.'''
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('nok'))

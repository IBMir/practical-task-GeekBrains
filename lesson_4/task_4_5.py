from task_2_3 import currency_rates
from sys import argv

try:
    question = argv[1]
except IndexError:
    question = ''

print(currency_rates(question))

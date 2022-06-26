import re

with open('nginx_logs.txt') as f:
    for i in f:
        result = []
        result.append(re.findall(r'^.+(?= - -)', i)[0])
        result += (re.findall(r'\d{2}/[^\]]+', i))
        result += (re.findall(r'GET', i))
        result += (re.findall(r'/d[^ H]+', i))
        result += ((re.findall(r'\d+ \d+', i,))[0]).split()
        print(result)

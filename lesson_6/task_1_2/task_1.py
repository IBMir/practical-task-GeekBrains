from pprint import pprint
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = list()
    for i in f:
        i = i.replace('"', '').split()
        intermediate_result = list()
        intermediate_result.append(i[0])
        intermediate_result.append(i[5])
        intermediate_result.append(i[6])
        intermediate_result = tuple(intermediate_result)
        result.append(intermediate_result)
    pprint(result)

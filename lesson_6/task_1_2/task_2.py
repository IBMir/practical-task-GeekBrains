with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    requests = dict()
    for i in f:
        i = i.replace('"', '').split()
        ip = i[0]
        if ip not in requests:
            requests[ip] = 0
        else:
            requests[ip] += 1
sorted_requests = sorted(requests.items(), key=lambda x: x[1])
print(sorted_requests[-1][0])


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
repeat = set()
for i in src:
    if i not in repeat:
        result.append(i)
    elif i in repeat and i in result:
        result.remove(i)
    repeat.add(i)

print(result)

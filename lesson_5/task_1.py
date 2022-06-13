def odd_nums(x):
    for i in range(1, x, 2):
        yield i

print(type(odd_nums))
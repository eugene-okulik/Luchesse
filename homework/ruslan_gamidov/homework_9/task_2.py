temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def hot(i):
    return i > 28


hot_list = list(filter(hot, temperatures))

print(hot_list)
print(min(hot_list))

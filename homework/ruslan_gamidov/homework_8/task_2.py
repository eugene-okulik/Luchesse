def fibo():
    x, y = 0, 1
    i = 0
    while True:
        i += 1
        yield x, i
        x, y = y, x + y


data = [5, 200, 1000, 100000]
index = 0

for xx, ii in fibo():
    if ii == data[index]:
        print(xx)
        index += 1
        if index == len(data):
            break

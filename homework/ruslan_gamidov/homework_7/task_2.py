words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    count = 0
    while True:
        print(key)
        count += 1
        if count == value:
            break

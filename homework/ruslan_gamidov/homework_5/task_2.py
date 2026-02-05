text = 'результат операции: 42'

index = text.index(':')
number = int(text[index + 2:])
print(number + 10)

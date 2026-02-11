while True:
    secret_num = 1
    user_num = int(input('Попробуй угадать цифру: '))
    if user_num != secret_num:
        print('попробуйте снова')
        continue
    print('Поздравляю! Вы угадали!')
    break

from random import randrange, choice


def func():
    salary = int(input('Какое число? '))
    bonus = choice([True, False])
    total_salary = salary
    if bonus:
        total_salary += randrange(1, 1000)
    return f'{salary}, {bonus} - "${total_salary}"'


print(func())

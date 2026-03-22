import os
from datetime import datetime, timedelta


def process_line(line_text):
    line_text = line_text.strip()
    if not line_text:
        return
    number_date, instruction = line_text.split(' - ', 1)
    date = number_date.split('. ', 1)[1]
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

    if 'на неделю позже' in instruction:
        print((dt + timedelta(weeks=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    elif 'день недели' in instruction:
        days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        print(days[dt.weekday()])
    elif 'сколько дней назад' in instruction:
        print((datetime.now() - dt).days)


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path, encoding='utf-8') as f:
    for line in f:
        process_line(line)

import os
import csv
from dotenv import load_dotenv
import mysql.connector as mysql

load_dotenv()

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME'),
)
cursor = db.cursor(dictionary=True)

missing = []
with open(csv_path, newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        query = """
                    SELECT * FROM students s
                    JOIN `groups` g ON s.group_id = g.id
                    JOIN books b ON s.id = b.taken_by_student_id
                    JOIN marks m ON s.id = m.student_id
                    JOIN lessons l ON m.lesson_id = l.id
                    JOIN subjects sub ON l.subject_id = sub.id
                    WHERE s.name = %s
                        AND s.second_name = %s
                        AND g.title = %s
                        AND b.title = %s
                        AND sub.title = %s
                        AND l.title = %s
                        AND m.value = %s
                """
        cursor.execute(query, [
            row['name'], row['second_name'], row['group_title'],
            row['book_title'], row['subject_title'], row['lesson_title'],
            row['mark_value']
        ])
        if len(cursor.fetchall()) == 0:
            missing.append(f"{row['name']} {row['second_name']}")

if missing:
    print("Отсутствующие студенты:")
    print("\n".join(missing))

db.close()

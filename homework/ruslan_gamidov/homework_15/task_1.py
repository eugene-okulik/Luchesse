import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ['Ruslan', 'Gamidov'])
student_id = cursor.lastrowid

cursor.executemany("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   [['Изучаем Python', student_id], ['Being a Playwright', student_id]])

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ['Automation QA', 'jan 2026', 'jun 2026'])
group_id = cursor.lastrowid

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", [group_id, student_id])

cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ['Biohacking'])
subj1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ['QAtoAQA'])
subj2_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ['lesson bio', subj1_id])
less1_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ['lesson hacking', subj1_id])
less2_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ['lesson QA', subj2_id])
less3_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ['lesson AQA', subj2_id])
less4_id = cursor.lastrowid

marks = [[10, less1_id], [9, less2_id], [8, less3_id], [7, less4_id]]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   [[v, lid, student_id] for v, lid in marks])

db.commit()

cursor.execute("SELECT value FROM marks WHERE student_id = %s", [student_id])
print([row['value'] for row in cursor.fetchall()])

cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", [student_id])
print([row['title'] for row in cursor.fetchall()])

cursor.execute("""
    SELECT g.title, b.title, m.value, l.title, s2.title
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects s2 ON s2.id = l.subject_id
    WHERE s.id = %s
""", [student_id])
for row in cursor.fetchall():
    print(row['g.title'], row['b.title'], row['value'], row['l.title'], row['s2.title'])

db.close()

class Book:
    material_pages = 'бумага'
    have_text = True

    def __init__(self, name_book, autor, count_pages, isbn, reserved=False):
        self.name_book = name_book
        self.autor = autor
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserved = reserved

    def visual(self):
        if self.reserved:
            return (f'Название: {self.name_book}, Автор: {self.autor}, страниц: {self.count_pages}, '
                    f'материал: {self.material_pages}, зарезервирована')
        else:
            return (f'Название: {self.name_book}, Автор: {self.autor}, страниц: {self.count_pages},'
                    f' материал: {self.material_pages}')


book1 = Book('Идиот', 'Достоевский', 500, '12345678')
print(book1.visual())

book2 = Book('Идиот', 'Достоевский', 500, '12345678', True)
print(book2.visual())

book3 = Book('Мастер и Маргарита', 'Булгаков', 600, '64634523')
print(book3.visual())

book4 = Book('Преступление и наказание', 'Достоевский', 400, '098765443')
print(book4.visual())

book5 = Book('Гуливер в стране лилипутов', 'Свифт', 300, '0192837465')
print(book5.visual())


class TextBook(Book):
    def __init__(self, name_book, autor, count_pages, isbn, subject, school_class, has_task, reserved=False):
        super().__init__(name_book, autor, count_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_task = has_task

    def visual(self):
        if self.reserved:
            return (f'Название: {self.name_book}, Автор: {self.autor}, страниц: {self.count_pages}, '
                    f'предмет: {self.subject}, класс: {self.school_class} зарезервирована')
        else:
            return (f'Название: {self.name_book}, Автор: {self.autor}, страниц: {self.count_pages},'
                    f' предмет: {self.subject}, класс: {self.school_class}')


tb1 = TextBook('Алгебра', 'Иванов', 200, '111333', 'Математика"', 9, True, reserved=False)
print(tb1.visual())

tb2 = TextBook('Алгебра', 'Иванов', 200, '444222', 'Математик', 10, False, reserved=True)
print(tb2.visual())

tb3 = TextBook('История России', 'Петров', 350, '555666', 'История', 11, True, reserved=True)
print(tb3.visual())

tb4 = TextBook('География', 'Сидоров', 180, '999777', 'География', 12, False, reserved=False)
print(tb4.visual())

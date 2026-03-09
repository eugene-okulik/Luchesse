class Flowers:
    def __init__(self, name, color, stem_len, fresh, price, life):
        self.name = name
        self.color = color
        self.stem_len = stem_len
        self.fresh = fresh
        self.price = price
        self.life = life

    def __str__(self):
        return (f'{self.name} ({self.color}), стебель: {self.stem_len}, свежесть: {self.fresh}, '
                f'цена: {self.price}, жизнь: {self.life} дней')


class Rose(Flowers):
    def __init__(self, name, color, stem_len, fresh, price, life):
        super().__init__(name, color, stem_len, fresh, price, life)


class Lily(Flowers):
    def __init__(self, name, color, stem_len, fresh, price, life):
        super().__init__(name, color, stem_len, fresh, price, life)


class Daisy(Flowers):
    def __init__(self, name, color, stem_len, fresh, price, life):
        super().__init__(name, color, stem_len, fresh, price, life)


class Bouquet:
    def __init__(self):
        self.flows = []

    def add(self, *args):
        for flow in args:
            self.flows.append(flow)

    def total_price(self):
        return sum(flow.price for flow in self.flows)

    def lifetime(self):
        return sum(flow.life for flow in self.flows) / len(self.flows) if self.flows else 0

    def sort_by_freshness(self):
        self.flows.sort(key=lambda x: x.fresh)

    def sort_by_color(self):
        self.flows.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flows.sort(key=lambda x: x.stem_len)

    def sort_by_price(self):
        self.flows.sort(key=lambda x: x.price)

    def find_by_color(self, color):
        found = []
        for flower in self.flows:
            if flower.color == color:
                found.append(f'{flower.name} ({flower.color})')
        if not found:
            return f'Цветы цвета - {color} не найдены'
        return ', '.join(found)

    def __str__(self):
        return '\n'.join(str(f) for f in self.flows)


rose1 = Rose('РозаЧили', 'красная', 40, 10, 7, 9)
rose2 = Rose('РозаОАЭ', 'белая', 35, 9, 6, 8)
daisy1 = Daisy('Гвоздика', 'желтый', 30, 6, 5, 7)
lily1 = Lily('Лилия', 'розовая', 45, 12, 8, 10)

bouquet = Bouquet()
bouquet.add(rose1, rose2, daisy1, lily1)

print(bouquet)
print(bouquet.total_price())
print(bouquet.lifetime())
bouquet.sort_by_price()
print(daisy1)
print(bouquet)
print(bouquet.find_by_color('желтый'))
print(bouquet.find_by_color('красная'))
print(bouquet.find_by_color('синий'))

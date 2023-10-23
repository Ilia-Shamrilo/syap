# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса.

class Bimbimbambam:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Bimbimbambam.count += 1

    @staticmethod
    def bimbim_count():
        return Bimbimbambam.count

    @classmethod
    def get_average_price(cls, bimbimbambams):
        total_price = 0
        for bim in bimbimbambams:
            total_price += bim.price
        return total_price / len(bimbimbambams)


item1 = Bimbimbambam("Телевизор", 5000)
item2 = Bimbimbambam("Холодильник", 2000)
item3 = Bimbimbambam("Телефон Poco x3 Pro", 1000)
item4 = Bimbimbambam("кроссовки", 100)

bimbim_count = Bimbimbambam.bimbim_count()
print(f"Всего вещей: {bimbim_count}")

bimbimbambams = [item1, item2, item3, item4]
average_price = Bimbimbambam.get_average_price(bimbimbambams)
print(f"Средняя цена всей продукции: {average_price}")

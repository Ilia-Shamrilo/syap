# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических
# свойства: _area и _price. Свои начальные значения они получают из
# параметров метода __init__()
# 3. Создайте метод final_price(), который принимает в качестве параметра
# размер скидки и возвращает цену с учетом данной скидки.
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он
# создавал объект с площадью 40м2
# Класс Human
# 1. Реализуйте приватный метод make_deal(), который будет отвечать за
# техническую реализацию покупки дома: уменьшать количество денег на
# счету и присваивать ссылку на только что купленный дом. В качестве
# аргументов данный метод принимает объект дома и его цену.
# 2. Реализуйте метод buy_house(), который будет проверять, что у человека
# достаточно денег для покупки, и совершать сделку. Если денег слишком
# мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка
# на дом и размер скидки

class House:

    def __init__(self, area, price, name):
        self._area = area
        self._price = price
        self.name = name

    def final_price(self, discount):
        return self._price - (self._price * discount / 100)

    def __str__(self):
        return self.name


class SmallHouse(House):
    def __init__(self, price, name):
        super().__init__(40, price, name)


class Human:
    def __init__(self, name, money):
        self._name = name
        self._money = money
        self._house = None

    def __str__(self):
        return self._name

    def make_deal(self, house, price):
        self._house = house
        if self._money >= price:
            self._money -= price
            print(f"{self} приобрёл: {self._house}")
        else:
            print(f"{self}, вам не хватило средств на: {self._house}")

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        self.make_deal(house, final_price)


house1 = House(100, 500000, 'дом')
house2 = SmallHouse(100000, 'домишко')

person = Human("Андрей", 500000)
person.buy_house(house1, 10)
person.buy_house(house2, 5)

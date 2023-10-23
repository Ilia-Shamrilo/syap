# Создать классы «Зоомагазин», «Животное», «Рыбы», «Птицы». Определить
# свойства: породу и стоимость для указанных животных (рыб, птиц), в
# каждом классе реализовать переопределение метода «способ передвижения».
# Вывести данные о самой дорогой породе. Предусмотреть метод записи
# информации в файл
class Zooshop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_max_price(self):
        expensive_bread = None
        max_price = 0
        for animal in self.animals:
            if animal.price > max_price:
                max_price = animal.price
                expensive_bread = animal.bread
        return expensive_bread

    def save_to_file(self, filename):
        with open("animal.txt", 'w') as file:
            for animal in self.animals:
                file.write(str(animal) + '\n')


class Animal:
    def __init__(self, bread, price):
        self.bread = bread
        self.price = price

    def move(self):
        pass

    def __str__(self):
        return f"Порода: {self.bread}, Цена: {self.price}"


class Fish(Animal):
    def move(self):
        return "Плавает"


class Bird(Animal):
    def move(self):
        return "Летает"


zooshop = Zooshop()

animal1 = Animal("корги", 5)
fish1 = Fish("золотая рыбка", 2)
bird1 = Bird("попугай", 20)
animal2 = Animal("Белка летяга", 25)

zooshop.add_animal(animal1)
zooshop.add_animal(fish1)
zooshop.add_animal(bird1)
zooshop.add_animal(animal2)

expensive_bread = zooshop.get_max_price()
print(f"Самая дорогая порода: {expensive_bread}")

zooshop.save_to_file("animal.txt")

# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических
# операций. А также функция, для ввода данных.

class Calculator:

    def sum(self, a, b):
        return a + b

    def min(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "на 0 делить нельзя"

    def input_num(self):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return a, b


calculator = Calculator()

a, b = calculator.input_num()

result = calculator.sum(a, b)
print("Сумма = ", result)

result = calculator.min(a, b)
print("Вычитание = ", result)

result = calculator.multi(a, b)
print("Произведение = ", result)

result = calculator.divide(a, b)
print("Частное = ", result)

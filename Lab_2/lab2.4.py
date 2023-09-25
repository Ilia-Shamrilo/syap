# Напишите программу, демонстрирующую работу try\except\finally
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Ошибка деления на ноль")
finally:
    print("Конец программы")

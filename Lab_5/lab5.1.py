# Вычисления с помощью NumPy
# 6 уравнение
import numpy as np

while True:
    try:
        x = float(input("Введите x: "))
        break
    except ValueError:
        print("неверный ввод")

y = (np.sin(np.pi / 2 + 1) ** 2 + x * np.power(3 + x ** 2, 1/4) - np.tan(x ** 3 -1) ** 3) / (np.arctan(x / 2) - np.log(17.56))
print(y)

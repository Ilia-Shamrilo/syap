# Визуализация данных в Matplotlib
# Работа с графиками и обработка массивов. Сформировать массив значений функции f(x) на заданном
# интервале по формуле из таблицы ниже. Вывести на экран значения аргумента и значения функции.
# Найти в массиве наибольшее, наименьшее, среднее значение, определить количество элементов массива,
# а также отсортировать его (чётные варианты – по убыванию, нечётные – по возрастанию). Построить график
# изменения значений функции, вывести на экран его с обозначением осей, пределов изменения функции и аргумента.
# На экран также вывести график прямой, значение которой равно среднему значению функции f(x). График прямой и
# функции оформить различными маркерами.

import numpy as np
import matplotlib.pyplot as plt

a_values = np.arange(3.5, 25.5,1.5)
x = 1.21
y_values = np.arcsin(x/3) + 1.2 * a_values

max_val = np.max(y_values)
min_val = np.min(y_values)
mean_val = np.mean(y_values)

print("Список аргументов функций: ", a_values)
print("Список значений функций: ", y_values)

print("Наибольшее значение функции: ", max_val)
print("Минимальное значение функции: ", min_val)
print("Среднее значение функции: ", mean_val)

count = len(y_values)
sorted_vals = np.sort(y_values)
print("Отсортированные по возрастанию значения функции f(x): ", sorted_vals)

plt.plot(a_values,y_values, label="f(x)")
mean_line = np.full_like(a_values, mean_val)
plt.plot(a_values, mean_line, label="среднее значение")
plt.legend(loc="lower right")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции f(x) + график среднего значения")
plt.grid(True)
plt.show()

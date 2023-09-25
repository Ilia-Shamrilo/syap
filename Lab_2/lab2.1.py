# Написать функцию triangle, принимающую 1 аргумент — сторону равностороннего треугольника,
# и возвращающую 2 значения (с помощью кортежа): площадь и высоту треугольника.
def triangle(size):
    area = (size ** 2 * (3 ** 0.5)) / 4
    height = (size * (3 ** 0.5)) / 2
    return (area, height)
side = int(input("Введите сторону равностороннего треугольника "))
area_height = triangle(side)
print(area_height)

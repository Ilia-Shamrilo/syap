# Имеется текстовый файл «Результаты соревнований», строка
# которого содержит в себе информацию: фамилия спортсмена, результат.
# Вывести на экран информацию о том, кто занял первое, второе и третье
# места. Пример файла:
# Иванов 2
# Петров 5
with open("result.txt", "r") as file:
    lines = file.read().split("\n")

results = []

for line in lines:
    surname, result = line.split()
    results.append((surname, int(result)))

results.sort(key=lambda x: x[1], reverse=True)

print("Первое место:", results[0][0])
print("Второе место:", results[1][0])
print("Третье место:", results[2][0])

# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# все строки, которые содержат только одно слово. Найти самое длинное слово
# в файле F2.
with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        f1.write(line + "\n")

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    for line in lines:
        if len(line.split()) == 1:
            f2.write(line)

with open("F2.txt", "r") as f2:
    lines = f2.readlines()
    longest_word = ""
    for line in lines:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

print("Самое длинное слово:", longest_word)

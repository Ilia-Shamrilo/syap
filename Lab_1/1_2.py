# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
# В случае равенства вывести на экран все согласные буквы. Посчитать количество слов в тексте.

text = input("Введите текст: ")

soglas_letters = 0
soglas_list = []
glas_letters = 0
word = 0

for letter in text:
    if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        soglas_letters += 1

    elif letter.lower() in 'aeiou':
        soglas_list.append(letter)
        glas_letters += 1

if glas_letters == soglas_letters:
    print(*soglas_list)
else:
    print("Количество согласных букв: ", soglas_letters)
    print("Количество гласных букв: ", glas_letters)
    print("Количество слов: ", len(text.split()))

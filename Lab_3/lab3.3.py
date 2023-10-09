# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
# 30}
def create_subject_dict():
    subject_dict = {}

    with open("dictionary.txt", 'r') as file:
        for line in file:
            if line:
                subject, activities = line.split(':')
                activities = activities.split()


                total_activities = 0
                for activity in activities:
                    count, type = activity.split('(')
                    count = int(count)
                    total_activities += count

                subject_dict[subject] = total_activities

    return subject_dict


print(create_subject_dict())

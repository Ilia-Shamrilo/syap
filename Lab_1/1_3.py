# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент. Преобразовать список так,
# чтобы сначала шли нулевые элементы, а затем все остальные.

l = list(map(int, input("Введите список, состоящий из чисел: ").split()))
min_num = l[0]
for i in range(1, len(l)):
    if l[i] % 2 == 0:
        if l[i] < min_num:
            min_num = l[i]

zero_elements = [num for num in l if num == 0]
other_elements = [num for num in l if num != 0]
res_list = zero_elements + other_elements

print(res_list)
print(min_num)

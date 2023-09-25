# Дана целочисленная прямоугольная матрица. Определить количество
# столбцов, не содержащих ни одного нулевого элемента.
def count_nonzero_columns(matrix):
    count = 0
    for col in range(len(matrix[0])):
        flag = False
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                flag = True
                break
        if not flag:
            count += 1
    return count


matrix = []
n = int(input("Введите количество строк матрицы : "))
print('Введите элементы матрицы')
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)

result = count_nonzero_columns(matrix)
print("Количество столбцов без нулевых элементов:", result)

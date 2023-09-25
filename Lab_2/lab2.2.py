# Напишите функцию, которая будет принимать один аргумент. Если в функцию передаётся словарь, найдите три ключа с самыми маленькими
# значениями в словаре
# Если список, то найти произведение между первым и вторым положительными элементами.
# Число – определить простое, или нет.
# Строка – определить самый повторяющийся символ.
# Сделать проверку со всеми этими случаями.
def analyze_input(arg):
    if type(arg) == dict:
        smallest_keys = sorted(arg, key=arg.get)[:3]
        return smallest_keys
    elif type(arg) == list:
        first = -1
        second = -2
        flag = True
        for i in range(0, len(arg)):
            if arg[i] > 0 and flag:
                first = i
                flag = False
                continue
            if arg[i] > 0 and not flag:
                second = i
                break
        if second == first + 1:
            return "перовое и второе положительное число стоят рядом"
        if second == -2 or first == -1:
            return "недостаточно положительных элементов"
        proiz = 1
        for i in range(first + 1, second):
            proiz *= arg[i]
        return proiz
    elif type(arg) == int:
        if arg < 2:
            return False
        for i in range(2, int(arg * 0.5) + 1):
            if arg % i == 0:
                return False
        return True
    elif type(arg) == str:
        char_count = {}
        for char in arg:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        max_count = max(char_count.values())
        for i in char_count:
            if char_count[i] == max_count:
                return i
    else:
        return "неверный ввод"


dictionary = {'a': 5, 'b': 2, 'c': 7, 'd': 1, 'e': 3}
print(analyze_input(dictionary))

numbers = [0, 4, -3, -6, 1, -5]
print(analyze_input(numbers))

number = 29
print(analyze_input(number))

string = "abracadabra"
print(analyze_input(string))

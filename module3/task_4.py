print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2

# Запрос длин катетов у пользователя
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

# Вычисление площади прямоугольного треугольника
S = (a * b) / 2

# Вывод результата
print("Площадь прямоугольного треугольника: ", S)

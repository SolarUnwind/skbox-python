print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения


def seat_students(b, g):
    seating = ""
    if (b > 2 * g) or (g > 2 * b):
        return "Нет решения"
    elif b >= g:
        k = b - g
        for bgb in range(k):
            seating += "BGB"
        for bg in range(g - k):
            seating += "BG"
    else:
        k = g - b
        for gbg in range(k):
            seating += "GBG"
        for gb in range(b - k):
            seating += "GB"

    return seating


b = int(input("Введите кол-во мальчиков: "))
g = int(input("Введите кол-во девочек: "))

result = seat_students(b, g)
print("Ответ:", result)
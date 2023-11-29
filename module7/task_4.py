print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

grades = input("Введите список оценок через пробел: ").split()
excellent = 0
good = 0
average = 0

for grade in grades:
    if int(grade) == 5:
        excellent += 1
    elif int(grade) == 4:
        good += 1
    else:
        average += 1

if excellent > good and excellent > average:
    print("Сегодня больше отличников")
elif good > excellent and good > average:
    print("Сегодня больше хорошистов")
else:
    print("Сегодня больше троечников")

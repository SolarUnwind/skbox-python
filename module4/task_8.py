print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

# Получаем ввод от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Используем условный оператор для определения максимального числа
if num1 > num2 and num1 > num3:
    max_num = num1
elif num2 > num1 and num2 > num3:
    max_num = num2
else:
    max_num = num3

# Выводим результат
print("Максимальное число: ", max_num)

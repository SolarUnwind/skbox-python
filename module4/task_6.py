print('Задача 6. Игра в кубики')

# Вася понимает, как важен отдых после тяжёлого рабочего дня, поэтому часто ходит в местный бар с друзьями. Владелец бара любит азартные игры и иногда предлагает посетителям с ним сыграть. Вася избегает азартные игры, но предложил владельцу купить у него программу для расчёта результатов игры, которую можно выводить на экраны бара.

# Напишите программу: на вход в неё подаётся два числа. Если первое число больше или равно второму, то нужно вывести на экран их разность и отдельной строкой: «Игрок платит». В противном случае, вывести их сумму и отдельной строкой: «Владелец платит». Последней строкой на экран должна быть выведена фраза: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена

# Получаем два числа от пользователя
cube_stranger = int(input("Кубик Кости: "))
cube_owner = int(input("Кубик владельца: "))

# Проверяем условие и выводим соответствующий результат
if cube_stranger >= cube_owner:
    discretion = cube_stranger - cube_owner
    print(f"Разность: {discretion}")
    print("Игрок платит")
else:
    summary = cube_stranger + cube_owner
    print(f"Сумма: {summary}")
    print("Владелец платит")

# Выводим завершающую строку
print("Игра окончена")

print('Задача 7. Игра «Угадай число»')

# В одной из практических работ мы делали задачу, где папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

number = int(input("Требуется загадать число юзернэйм: "))
attempts = 0

while True:
    guess = int(input("Введите число: "))
    attempts += 1
    if guess < number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif guess > number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print(f"Вы угадали! Число попыток: {attempts}")
        break

print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришли,
# перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


import random

def rock_paper_scissors():
    options = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(options)
    user_choice = input("Введите камень, ножницы или бумага: ").lower()

    if user_choice not in options:
        print("Неверный ввод. Попробуйте еще раз.")
    else:
        print(f"Компьютер выбрал: {computer_choice}")
        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
            print("Вы победили!")
        else:
            print("Вы проиграли.")

def guess_the_number():
    secret_number = random.randint(1, 100)
    while True:
        user_guess = int(input("Угадайте число от 1 до 100: "))
        if user_guess < secret_number:
            print("Загаданное число больше.")
        elif user_guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число: {secret_number}")
            break

def mainMenu():
    while True:
        print("\nГлавное меню:")
        print("1 - Игра 'Камень, ножницы, бумага'")
        print("2 - Игра 'Угадай число'")
        print("0 - Выход")
        choice = input("Введите номер игры: ")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            guess_the_number()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск главного меню игры
mainMenu()

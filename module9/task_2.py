print('Задача 2. Кривой мессенджер')

# Существует мессенджер, в котором иногда возникают неполадки при передаче сообщений: в них попадает лишний символ — звёздочка. Пользователям это надоело, поэтому они стали уходить в другие сервисы. Но один из них заинтересовался, на каких позициях обычно появляется звёздочка. Чтобы выяснить это, пользователю необходимо подготовить строки, в которых символ «*» встречается ровно один раз.

# Что нужно сделать:

# Напишите программу, которая определяет порядковый номер звёздочки в строке.

# Пример:

# Введите текст: «Пр*ивет как дела».
# Символ «*» стоит на позиции 3.

text = input("Введите текст: ")

index = text.find("*")

if index != -1:
    position = index + 1
    print(f"Символ '*' стоит на позиции {position}.")
else:
    print("Символ ‘*’ не найден в строке.")

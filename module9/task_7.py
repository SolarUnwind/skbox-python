print('Задача 7. Метод бутерброда')

# В секретном агентстве Super-Secret-no решили использовать «метод бутерброда» для шифрования переписки своих сотрудников. Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, последняя буква — номер 2, вторая — номер 3, предпоследняя — номер 4, потом третья… и так для всех букв (см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.

# Например, слово «sandwich» зашифруется в «shacnidw».
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.

# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
# Шифр:  | s | h | a | c | n | i | d | w |


encrypted_message = input("Введите зашифрованное сообщение: ")
decrypted_message = ""

accu1 = ' '
accu2 = ' '
count = 0

for cyphertext in encrypted_message:
    count += 1
    if (count % 2 == 1):
        accu1 += cyphertext
    else:
        accu2 = cyphertext + accu2

decrypted_message = accu1 + accu2
print("Расшифрованное сообщение:", decrypted_message)

# Kryptor
# message = input("Введите сообщение для шифровки: ")

# encrypted_message = ""

# for i in range(len(message) // 2):
#     encrypted_message += message[i] + message[len(message) - i - 1]

# if len(message) % 2 != 0:
#     encrypted_message += message[len(message) // 2]

# print("Зашифрованное сообщение:", encrypted_message)

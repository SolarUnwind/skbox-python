print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29


levels = int(input("Введите количество уровней пирамиды: "))
current_number = 1

for row in range(levels):
    print('\t' * (levels - row - 1), end="")
    for col in range(row + 1):
        print(current_number, end="")
        current_number += 2
        print('\t' * 2, end = "")
    print()

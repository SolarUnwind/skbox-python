print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345


level = int(input("Введите число: "))
width = level * 2

for col in range(1, level+1):
    print_num = level

    for row in range(width):
        if row < col:
            print(print_num, end="")
            print_num -= 1
        elif row > width - 1 - col:
            print_num += 1
            print(print_num, end="")
        else:
            print(".", end="")

    print()

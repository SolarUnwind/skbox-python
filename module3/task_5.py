print('Задача 5. Часы')

# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

# Получение количества минут от пользователя
n = int(input("Введите количество минут: "))

# Вычисление количества часов и оставшихся минут
hours = n // 60
remaining_minutes = n % 60

# Вывод результатов
print(f"{n} минут(а) это {hours} час(ов) и {remaining_minutes} минут(а)")

print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

sum_salary = 0

for i in range(1, 13):
    salary = float(input(f"Введите зарплату за месяц {i}: "))
    sum_salary += salary

average_salary = sum_salary / 12
print(f"Средняя зарплата за год: {average_salary}")

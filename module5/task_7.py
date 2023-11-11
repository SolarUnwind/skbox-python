print('Задача 7. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».

# Первый способ (можно получить посылку):
# Вариант 1: Можно получить посылку
hour = int(input("Введите время в часах (от 0 до 23): "))

if (8 <= hour < 10 or 12 <= hour < 14 or 15 <= hour < 18 or 20 <= hour < 22):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")

#Второй способ (посылку получить нельзя):
hour = int(input("Введите время в часах (от 0 до 23): "))

if (0 <= hour < 8 or 10 <= hour < 12 or 14 <= hour < 15 or 18 <= hour < 20 or 22 <= hour):
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")
print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd(60, 48))  # Выведет: 12


# начиная с версии Python 3.5, есть встроенная функция math.gcd, которая делает то же самое:
import math

print(math.gcd(60, 48))  # Выведет: 12

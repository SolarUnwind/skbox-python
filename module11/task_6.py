print('Задача 6. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

def round_coordinate(coord):
    return int(coord * 10)

def within_board(coord):
    return 0 <= coord <= 7

# Получение координат коня и точки
try:
    x1 = float(input("Введите местоположение коня:\n"))
    y1 = float(input())
    x2 = float(input("Введите местоположение точки на доске:\n"))
    y2 = float(input())
except ValueError:
    print("Вы ввели некорректные координаты.")
    exit()

# Округление координат
x1 = round_coordinate(x1)
y1 = round_coordinate(y1)
x2 = round_coordinate(x2)
y2 = round_coordinate(y2)

# Проверка, что координаты находятся в пределах шахматной доски
if not within_board(x1) or not within_board(y1) or not within_board(x2) or not within_board(y2):
    print("Введены некорректные координаты.")
    exit()

print(f"Конь в клетке {(x1, y1)}. Точка в клетке {(x2, y2)}.")

# Проверка, что конь может ходить в эту точку
diff_x = abs(x1 - x2)
diff_y = abs(y1 - y2)
if (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1):
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")

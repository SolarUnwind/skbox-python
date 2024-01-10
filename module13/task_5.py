print('Задача 5. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний


# Функция для подсчета количества колебаний до остановки маятника
def count_swing(amplitude_start, amplitude_stop):
    count = 0
    while amplitude_start > amplitude_stop:
        amplitude_start *= (1 - 0.084)
        count += 1
    return count

# Функция для контроля ввода данных пользователем
def input_control(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                raise ValueError("Введите положительное число больше нуля.")
            return value
        except ValueError as e:
            print(e)

# Основная часть программы
def main():
    amplitude_start = input_control("Введите начальную амплитуду в сантиметрах: ")
    amplitude_stop = input_control("Введите амплитуду остановки в сантиметрах: ")

    if amplitude_stop >= amplitude_start:
        print("Амплитуда остановки должна быть меньше начальной амплитуды.")
        return

    swings = count_swing(amplitude_start, amplitude_stop)
    print(f"Маятник считается остановившимся через {swings} колебаний")


main()

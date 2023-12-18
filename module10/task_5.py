print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.


# функция, которая для заданного числа вычисляет сумму его цифр
def get_digit_sum(num):
    return sum(map(int, str(num)))

def find_largest_digit_sum():
    num_list = input("Введите числа через пробел: ").split()

    largest_num = None
    largest_sum = 0

    for num in num_list:
        digit_sum = get_digit_sum(int(num))
        if digit_sum > largest_sum:
            largest_num = num
            largest_sum = digit_sum

    print(f"Наибольшее число по сумме цифр: {largest_num}")
    print(f"Сумма его цифр: {largest_sum}")

find_largest_digit_sum()

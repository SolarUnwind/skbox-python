print('Задача 6. Коровы')

# Для коров есть 10 стойл. В каждом из них условия для животных разные, поэтому и молока они дают по-разному. В первом стойле производят 2 литра в день, во втором — 4, в третьем — 6, далее — 8, 10, 12, 14, 16, 18 и 20. При этом коровы находятся не во всех стойлах. Свободные и занятые обозначаются строкой из букв a и b, где a — свободное стойло, b — занятое.

# Что нужно сделать

# Напишите программу для подсчёта получаемого молока в коровнике. Важно учитывать следующее взаимодействие: пользователь вводит строку из десяти символов a и b. Необходимо определить, сколько в итоге будет произведено молока за день.

cows = input("Введите строку состояний стойл (a - свободное, b - занятое): ")

milk_per_day = 0

for i in range(len(cows)):
    if cows[i] == "b":
        milk_per_day += (i+1)*2

print("Всего произведено молока за день:", milk_per_day, "литров")

print('Задача 1. Я стал новым пиратом!')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек. Те, кто крикнет слово «Карамба», попадут на борт.

# Что нужно сделать

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

words = []

for i in range(1, 11):
    word = input(f"Введите слово {i}: ").lower()
    words.append(word)

karamba_count = words.count("карамба")
print("Количество слов, совпадающих со словом ‘Карамба’:", karamba_count)

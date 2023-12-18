print('Задача 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

count = int(input("Введите количество чисел: "))
prime_count = 0

for i in range(count):
    num = int(input("Введите число: "))
    if is_prime(num):
        prime_count += 1

print("Количество простых чисел в последовательности:", prime_count)

# Решение задачи на Haskell. Это ведь ожидалось?

# isPrime :: Integer -> Bool
# isPrime n
#     | n <= 1    = False
#     | otherwise = null [x | x <- [2..floor (sqrt (fromIntegral n))], n `mod` x == 0]

# countPrimes :: [Integer] -> Int
# countPrimes nums = length [x | x <- nums, isPrime x]

# main :: IO ()
# main = do
#     putStrLn "Enter a list of numbers separated by commas:"
#     input <- getLine
#     let numStrings = words (map (\c -> if c == ',' then ' ' else c) input)
#         nums = map read numStrings :: [Integer]
#         result = countPrimes nums
#     putStrLn $ "The number of prime numbers in the list is " ++ show result

# $ ghc count-primes.hs
# [1 of 1] Compiling Main             ( count-primes.hs, count-primes.o )
# Linking count-primes ...
# $ ./count-primes
# Enter a list of numbers separated by commas:
# 4,7,20,3,11,37
# The number of prime numbers in the list is 4

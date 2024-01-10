-- Решение на Haskell задачи №3:
-- Вычисление факториала на языке Haskell.
-- По сути - это своего рода Haskell "Hello World!"
-- Вариант 1:

fac1 :: (Integral a) => a -> a
fac1 n = product [1..n]

-- Вариант 2:
fac2 :: (Integral a) => a -> a
fac2 0 = 1
fac2 n = n * fac2 (n - 1)


main :: IO ()
main = do
  putStrLn "Введите число для вычисления факториала: "
  input <- getLine
  let number = read input :: Int
  putStrLn "Вычисленный факториал 1 = "
  print $ fac1 number

  putStrLn "Вычисленный факториал 2 = "
  print $ fac2 number

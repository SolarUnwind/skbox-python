-- Решение на Haskell задачи №7:

sumSequence :: Int -> Double
sumSequence n = sum [(-1)**fromIntegral i * (1/2)**fromIntegral i | i <- [0..n]]


-- Функция sumSequence принимает на вход число n и использует генератор списка для создания списка с элементами последовательности.
-- Затем с помощью функции sum суммируются все элементы списка.

main :: IO ()
main = do
  let n = 4
  let result = sumSequence n
  putStrLn $ "Сумма элементов последовательности при N = " ++ show n ++ " равна " ++ show result

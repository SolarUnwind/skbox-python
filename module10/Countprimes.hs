-- Решение задачи №4 на Haskell. Это ведь ожидалось?

isPrime :: Integer -> Bool
isPrime n
    | n <= 1    = False
    | otherwise = null [x | x <- [2..floor (sqrt (fromIntegral n))], n `mod` x == 0]

countPrimes :: [Integer] -> Int
countPrimes nums = length [x | x <- nums, isPrime x]

main :: IO ()
main = do
    putStrLn "Enter a list of numbers separated by commas:"
    input <- getLine
    let numStrings = words (map (\c -> if c == ',' then ' ' else c) input)
        nums   = map read numStrings :: [Integer]
        result = countPrimes nums
    putStrLn $ "The number of prime numbers in the list is " ++ show result

-- $ ghc CountPrimes.hs
-- $ ./CountPrimes
-- Enter a list of numbers separated by commas:
-- 4,7,20,3,11,37
-- The number of prime numbers in the list is 4

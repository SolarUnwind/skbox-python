 -- В рамках программы колонизации Марса
 -- компания «Спейс Инжиниринг» вывела особую породу черепах,
 -- которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте....

 -- Ну что котятки, соскучились по Haskell'у ? Ну тогда вот решение
 -- той же задачи № 6, но на Haskell !!

-- Define the danger level function based on the given formula
dangerLevel :: Float -> Float
dangerLevel x = x**3 - 3*x**2 - 12*x + 10

-- Implement the safe depth search using a recursive function
findSafeDepth :: Float -> Float -> Float -> Float
findSafeDepth epsilon left right
    | abs (right - left) <= epsilon = (left + right) / 2
    | dangerLevel middle * dangerLevel left <= 0 = findSafeDepth epsilon left middle
    | otherwise = findSafeDepth epsilon middle right
    where middle = (left + right) / 2

-- Main function to interact with the user
main :: IO ()
main = do
    putStrLn "Enter the maximum permissible level of danger:"
    input <- getLine
    let epsilon = read input :: Float
    if epsilon <= 0 then
        putStrLn "Please enter a positive number greater than zero."
    else do
        let depth = findSafeDepth epsilon 0 4
        putStrLn $ "Approximate depth of safe laying: " ++ show depth ++ " m"

-- $ ghc SafeDepth.hs
-- $ ./SafeDepth
-- Enter the maximum permissible level of danger:
-- 0.01
-- Approximate depth of safe laying: 0.73046875 m

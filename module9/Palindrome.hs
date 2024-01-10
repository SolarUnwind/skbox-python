-- Определение палиндрома на Haskell. Задача № 8
isPalindrome :: String -> Bool
isPalindrome str = str == reverse str

main :: IO ()
main = do
  putStrLn "Введите строку для проверки на палиндром: "
  input <- getLine
  if isPalindrome input
    then putStrLn "Да, это палиндром!"
    else putStrLn "Нет, это не палиндром!"

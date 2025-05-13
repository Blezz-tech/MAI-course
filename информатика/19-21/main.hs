-- 20<S<100
-- S = 19 Победа

main :: IO ()
main = do
  -- putStrLn $ show (1, xs1) -- Петя1
  -- putStrLn $ show (2, xs2) -- Ваня1
  -- putStrLn $ show (3, xs3) -- Петя2

  -- putStrLn . show $ and [True, True, False]

  -- putStrLn $ show $
  putStrLn . show $
  -- putStrLn . show $ checker [18,18,18,15,15,15,6,6,6]



s_xs = [100,99..20]

f_filtered_s_xs = filter (\(x)) $ map f_results s_xs

f_results s = ( or $ checker xs1 -- 1: Петя1
              , or $ checker xs2 -- 2: Вова1
              , or $ checker xs3 -- 3: Петя2
              )
  where
    xs1 = f [s,s,s]
    xs2 = f xs1
    xs3 = f xs2

-- checker :: [Int] -> [Bool]
checker = map (<= 19)

-- f :: [Int] -> Int -> ([Int], Int)
f xs = (map (\x -> x-2) xs) ++ (map (\x -> x-5) xs) ++ (map (`div` 3) xs)


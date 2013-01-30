-- http://projecteuler.net/problem=19

-- 1 Jan 1901 was a Tuesday (365 `mod` 7)
months :: Int -> [Int]
months x
  | leap x = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  | otherwise = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leap :: Int -> Bool
leap x = x `mod` 4 == 0 && x `mod` 100 /= 0 || x `mod` 400 == 0

sundays :: [Int]
sundays = filter isSunday $ scanl (+) 1 $ concatMap months [1901 ..2000]
  where isSunday x = x `mod` 7 == 6

res :: Int
res = length sundays

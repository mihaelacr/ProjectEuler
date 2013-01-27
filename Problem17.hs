-- http://projecteuler.net/problem=17

nrToStringCount :: Int -> Int
nrToStringCount n
  | n >= 1000 = error "Unsupported number! Too big"
  | n <= 12 = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6] !! (n - 1)
  | n `elem` [13, 15, 18] = 3 + nrToStringCount (n - 10)
  | n <= 19 = 4 + nrToStringCount (n - 10)
  | n == 70 = 7
  | n `elem` [40, 50, 60] = 5
  | n `elem` [20, 30, 80, 90] = 6
  | n < 100 = let rest = n `mod` 10 in nrToStringCount (n - rest) + nrToStringCount rest
  | n `mod` 100 == 0 = 7 + nrToStringCount (n `div` 100)
  | otherwise = let rest = n `mod` 100
                in 3 + nrToStringCount (n - rest) + nrToStringCount rest

res :: Int
res = 11 + sum (map nrToStringCount [1.. 999])

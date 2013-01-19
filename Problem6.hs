-- http://projecteuler.net/problem=6

f :: Int -> Int
f n = ((n * (n + 1)) `div` 2 ) ^ 2 - ((n * (n + 1) * (2 * n + 1)) `div` 6)

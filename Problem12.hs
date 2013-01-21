-- http://projecteuler.net/problem=12
import Sieve

limit:: Int
limit = 500

-- Computes the number of divisors of a number
nrDivs :: Int -> Int
nrDivs n = 2 * (1 + length [i | i<- [2 .. floor $ sqrt $ fromIntegral n ], n `mod` i == 0])

-- Computes the n'th triangular number
triangular :: Int -> Int
triangular n = n * (n + 1) `div` 2

-- Computes the number of divisors of a triangular number
-- by taking into account that gcd(n, n+1) = 1
nrDivTriangular :: Int -> Int
nrDivTriangular n
  | odd n = nrDivs n * (nrDivs ((n + 1) `div` 2))
  | otherwise = nrDivs (n `div` 2) * (nrDivs (n + 1))


res :: Int
res = triangular $ head $ dropWhile (\x -> nrDivTriangular x < limit) [1 ..]

-- Computes the number of divisors using Euler's function, but it is more
-- expensice than simple version nrDivs (above)
nrTimes n p = nrTimes' n p 0
nrTimes' n p i
  | n `mod` p == 0 = nrTimes' (n `div` p) p (i + 1)
  | otherwise = i

-- Uses Euler's function to compute the number of divisors
nrDivs2 :: Int -> Int
nrDivs2 n = product [nrTimes n p + 1| p <- pDivs]
  where ps = takeWhile (\x ->  x <= (fromIntegral $ n `div` 2)) primes
        pDivs = [p | p <- map fromIntegral ps , n `mod` p == 0]

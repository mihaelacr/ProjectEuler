-- http://projecteuler.net/problem=15

-- Note that it is more efficient to implement choose like this instead of
-- using factorial
choose :: Int -> Int -> Int
choose _ 0 = 1
choose 0 _ = 0
choose n k = choose (n - 1) (k - 1) * n `div` k

-- The number of ways of getting from (0,0) to (m,n) without backtracking
-- is choose (m+n) n
res :: Int
res = choose 40 20

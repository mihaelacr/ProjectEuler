-- http://projecteuler.net/problem=5

-- 2 5
-- 3 2
-- 5 1
-- 7 1
-- 11 1
-- 13 1
-- 17
-- 19

res = 2 ^ 5 * 3 ^ 2 * 5 * 7 * 11 * 13 * 17 * 19

check = all even [ res `div` x | x <- [1..20]]

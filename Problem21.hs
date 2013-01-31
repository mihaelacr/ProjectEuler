-- http://projecteuler.net/problem=21
import Data.List
import qualified Data.Map as M

limit :: Int
limit = 10000

d :: Int -> Int
d n = 1 + sum [i | i <- [2 .. n `div` 2], n `mod` i == 0]


l1 :: [(Int, Int)]
l1 = [(i , d_i) | i  <- [1 .. limit], let d_i = d i, d_i /= i]

m1:: M.Map Int Int
m1 = M.fromList l1

f :: M.Map Int Int -> Int -> Int -> Int -> Int
f m k val s = if (M.lookup val m == Just k) && (k /= val) then s + k
                                                          else s
sol1 :: Int
sol1 = M.foldWithKey (f m1) 0 m1

l2 :: [(Int, Int)]
l2 = [(a, b) | (b, a) <- l1]

sol2 :: Int
sol2 = sum $ map fst $ intersect l1 l2

sol3 :: Int
sol3 =  sum [x | (x, y) <- zip [1 .. limit] [d (d i) | i <- [ 1.. limit] ], x == y, d x /= x]

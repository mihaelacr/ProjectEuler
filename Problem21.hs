-- http://projecteuler.net/problem=21
import Data.List
import qualified Data.Map as M

limit :: Int
limit = 10000

d :: Int -> Int
d n = 1 + sum [i | i <- [2 .. n `div` 2], n `mod` i == 0]

l1 :: [(Int, Int)]
l1 = [(i , d_i) | i  <- [1 .. limit], let d_i = d i, d_i /= i]
l2 :: [(Int, Int)]
l2 = [(a, b) | (b, a) <- l1]:

m1 = M.fromList l1
m2 = M.fromList l2

f :: M.Map Int Int -> Int -> Int -> Int -> Int
f m k val s = if (M.lookup val m == Just k) && (k /= val) then s + k
                                                          else s
sum1 :: Int
sum1 = M.foldWithKey (f m1) 0 m1


sm :: Int
sm = sum $ map fst $ intersect l1 l2

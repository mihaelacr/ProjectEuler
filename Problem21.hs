-- http://projecteuler.net/problem=21
module Problem21 where

import qualified Data.Map as M

limit :: Int
limit = 10000

d :: Int -> Int
d n = surplus + sum fst1 + sum snd1
 where fst1 = [i | i <- [2 .. lim], n `mod` i == 0]
       snd1 = [ n `div` k | k <- fst1]
       lim = floor $ sqrt $ fromIntegral n
       surplus = if lim * lim == n && lim /= 1 then 1 - lim else 1

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
sol2 =  sum [x | (x, y) <- zip [1 .. limit] [d (d i) | i <- [ 1.. limit] ], x == y, d x /= x]

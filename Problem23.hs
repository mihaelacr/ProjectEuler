import Data.Set
-- http://projecteuler.net/problem=23
import Problem21

isAbundant :: Int -> Bool
isAbundant x = d x > x

start:: Int
start = 12
stop :: Int
stop = 28123

find :: [Int] -> [Int] -> Int -> Int
find [] _ s = s
find (x:xs) abund s
  = if isAbundant x then find xs (x:abund) (s + add)
                    else find xs abund (s + add)
      where ms = any isAbundant [ x - n | n <- abund]
            add = if ms then 0 else x


res :: Int
res = find [start .. stop] [] 0 + 66

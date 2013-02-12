import qualified Data.Set as S
-- http://projecteuler.net/problem=23
import Problem21


start:: Int
start = 12
stop :: Int
stop = 28123


isAbundant :: Int -> Bool
isAbundant x = d x > x


find :: [Int] -> [Int] -> Int -> Int
find [] _ s = s
find (x:xs) abund s
  = if isAbundant x then find xs (x:abund) (s + add)
                    else find xs abund (s + add)
      where ms = any isAbundant [ x - n | n <- abund]
            add = if ms then 0 else x

res :: Int
res = find [start .. stop] [] 0 + 66


res' :: Int
res' = sum unwritables
  where
    abundants = filter isAbundant [start .. stop]
    unwritables = filter unwritable [start .. stop]
    unwritable x = any isAbundant [ x - n | n <- takeWhile (< x) abundants ]


main = print res'

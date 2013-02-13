import qualified Data.Set as S
-- http://projecteuler.net/problem=23
import Problem21

-- TODO: Replace "any isAbundant" by set-lookup (O(log n)) or array lookup (O(1))

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
res' = 66 + sum unwritables
 where
   l = [start .. stop]
   abundants = filter isAbundant l
   unwritables = filter (not . writable) l
   writable x = any isAbundant [ x - n | n <- takeWhile (< x) abundants ]


-- main = mapM print (take 100 res')
main = print res


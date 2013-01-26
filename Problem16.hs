-- http://projecteuler.net/problem=16
import Data.Char


-- TODO see most efficient implementation of power
nr :: Integer
nr = 2 ^ (1000 :: Integer)

digits :: [Int]
digits = [digitToInt n | n <- show nr]

res :: Int
res = sum digits

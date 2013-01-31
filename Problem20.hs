-- http://projecteuler.net/problem=20
import Data.Digits

fact :: Integer -> Integer
fact n = f n 1
  where f 0 p = p
        f n p = f (n-1) (p * n)

sol = sum $ digits 10 (fact 100)

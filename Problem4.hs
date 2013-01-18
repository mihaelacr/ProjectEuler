-- http://projecteuler.net/problem=4

-- idea start from the biggest number 999999
-- efficient way of checking a pallindrome
-- how to check a number is a product of 2 numbers less than 1000

-- the question is, what is less efficient: finding that something is a palindrome
-- or

import Data.Digits

possible :: [Integer]
possible = [999999, 999998 .. 10000]


isSymmetric :: Eq a => [a] -> Bool
isSymmetric xs = all (\i -> xs !! i == xs !! (l - i)) [0.. l `div` 2]
  where l = length xs - 1

isPalindrom :: Integer -> Bool
isPalindrom n = isSymmetric $ digits 10 n

isProduct :: Integer -> Bool
isProduct n = (dropWhile (not . (isP n)) [100 ..floor $ sqrt $ fromIntegral n]) /= []
  where has3 x = (x `div` 100 > 0) && (x `div` 100 < 10)
        isDiv n x = n `mod` x == 0
        other3 n x = has3 (n `div` x)
        isP n x = isDiv n x && other3 n x

-- it is cheaper to find out if a numver is a palindrom than to check all its divisors
pali = filter isPalindrom possible

maxProd = head $ filter isProduct pali


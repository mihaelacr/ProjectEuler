-- http://projecteuler.net/problem=2

limit :: Integer
limit = 4000000

fib :: [Integer]
fib = 0 : (1 : zipWith (+) fib (tail fib))

evens :: [Integer]
evens = filter even fib

res :: Integer
res = sum $ takeWhile (< limit) evens




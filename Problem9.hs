-- http://projecteuler.net/problem=9

pitagora :: (Int, Int, Int) -> Bool
pitagora (a, b, c) = a ^ 2 + b ^ 2 == c ^ 2

(p1, p2, p3) = head $ filter pitagora[ (a, b, 1000 - a - b )| a <- [0 .. 334], b <- [a .. 1000], 1000 - a - b > b]


prod = p1 * p2 * p3


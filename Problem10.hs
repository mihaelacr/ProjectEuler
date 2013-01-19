-- http://projecteuler.net/problem=10
import Sieve

limit = 2000000

s = sum (takeWhile (<limit) primes)


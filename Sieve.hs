module Sieve where

import Data.List.Ordered (minus)


-- Compute list of prime numbers using Sieve of Eratosthenes

-- The importance of lazy patterns is crucial!

-- see http://www.haskell.org/haskellwiki/Prime_numbers#Sieve_of_Eratosthenes
-- works on sequences, by looking at slots between consecutive squares of primes
-- and removing non primes between them
primes = 2 : primes'
  where
    primes' = sieve 3 9 primes' []
    -- fs is an accumulator of the type (2 p,  biggest multiple of p smaller than q) where p is a prime already in primes'
    -- (x, q) is the current range, from which we remove the patterns. exists t prime such that x = t ^ 2 + 2 and q = (t + 1) ^ 2
    sieve x q ~(p:t) fs =
        -- this foldr ensures that all the primes up to q are already in the list (and no non primes less than q are in the list)
        -- this is done by filtering out the multiples of ps which are in fs
        foldr (flip minus) [x, x+2..q-2]
                           [[y+s, y + 2 *s..q] | (s, y) <- fs]  -- remove all non primes in the current rage: note it is crucial that s / 2 | y
                                                                -- as s/ 2 is the prime we want to remove

        -- note that when you call this q is p ^ 2 so you remove the multiples of p smaller than p  ^ 2
        -- the steps remain the same (we did not remove any multiple of a prime number after the last square)
        -- however, we are changing the starting range, for efficiency
        -- note that we substract from q as the list above starts with y+s
        -- remember that y was divisible by s1 (where s1 is prime and s = 2 * s1), and we
        -- need to preserve that invariant in order to be able to remove multiples of s1
        ++ sieve (q + 2) (head t ^2) t ((2 * p, q):[(s, q-rem (q - y) s) | (s, y) <- fs])

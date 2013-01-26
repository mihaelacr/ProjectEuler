module Main where

import Data.Maybe
import Data.Map as M
import Data.List

type Storage = Map Int Int

limit :: Int
limit = 10 ^ (6:: Int)

f :: Int -> Int
f x
  | even x = x `div` 2
  | otherwise = 3 * x + 1


-- Gets the Collatz sequence (without the 1, but this is uneeded for comparison)
getSequence :: Int -> [Int]
getSequence 1 = []
getSequence n = n: takeWhile (/= 1) (iterate f n)


-- Computes the length Collatz sequence of n by using the already computes values given in seqs
getSequenceLength :: Int -> Storage -> Storage
getSequenceLength n seqs
  | even n = M.insert n  (1 + fromJust (M.lookup (f n) seqs))  seqs
  | otherwise = let (partial, rest) = span (>= n) $ getSequence n -- lazy evaluation at its best
                                                                  -- rest never gets computed, apart from it's head
                    additional = length partial
                    newLengths =  [additional , -1 .. 1]
                in case rest of
                  [] -> M.insert n additional seqs
                  (r : _) -> M.fromList (zip partial $ Prelude.map (+ fromJust (M.lookup r seqs)) newLengths) `M.union` seqs


-- Computes all the sequence lengths by storing what has been computed already
getAllSequenceLengths :: Int -> Storage -> Storage
getAllSequenceLengths n seqs
  | n >= limit = seqs
  | otherwise = getAllSequenceLengths (n + 1) (getSequenceLength n seqs)


maximumBySecond :: Ord b => [(a, b)] -> (a, b)
maximumBySecond = maximumBy sndOrd
  where sndOrd (_, y1) (_, y2) = compare y1 y2

maxSeq :: (Int, Int)
maxSeq = maximumBySecond $ M.toList $ getAllSequenceLengths 1 M.empty

maxSeqBruteForce :: (Int, Int)
maxSeqBruteForce = maximumBySecond [(i, length $ getSequence i) | i <- [1 .. limit + 1]]

main :: IO()
main = print maxSeqBruteForce

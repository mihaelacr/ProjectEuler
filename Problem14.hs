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

getInfiniteSequence :: Int -> [Int]
getInfiniteSequence n = f n : getInfiniteSequence (head $ getInfiniteSequence n)

-- Gets the Collatz sequence (without the 1, but this is uneeded for comparison)
getSequence :: Int -> [Int]
getSequence 1 = []
getSequence n = n: takeWhile (/= 1) (getInfiniteSequence n)


getSequence1 :: Int -> Storage -> Storage
getSequence1 n seqs
  | even n = M.insert n  (1 + fromJust (M.lookup (f n) seqs))  seqs
  | otherwise = let (partial, rest) = span (>= n) $ getSequence n
                    additional = length partial
                    newLengths =  [additional , -1 .. 1]
                in case rest of
                  [] -> M.insert n additional seqs
                  (r : _) -> M.fromList (zip partial $ Prelude.map (+ fromJust (M.lookup r seqs)) newLengths) `M.union` seqs


m1 :: Int -> Storage -> Storage
m1 n seqs
  | n >= limit = seqs
  | otherwise = m1 (n + 1) (getSequence1 n seqs)


sndOrd :: Ord b => (a, b) -> (a, b) -> Ordering
sndOrd (_, y1) (_, y2) = compare y1 y2

maxSeq :: (Int, Int)
maxSeq = maximumBy sndOrd $ M.toList $ m1 1 M.empty

maxSeqBruteForce :: (Int, Int)
maxSeqBruteForce = maximumBy sndOrd [(i, length $ getSequence i) | i <- [1 .. limit + 1]]

main :: IO()
main = print (maximumBy sndOrd [(i, length $ getSequence i) | i <- [1 .. limit + 1]])

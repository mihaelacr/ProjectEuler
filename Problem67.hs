module Problem67 where
-- http://projecteuler.net/problem=67
-- this solution also works for problem 18

filename :: String
filename = "Problem67.txt"

filename1 :: String
filename1 = "sample.txt"

-- precondition is that the argument is a triangular list
getMaxSum :: [[Int]] -> Int
getMaxSum [] = 0
getMaxSum xs = head $ foldr f (last xs) (init xs)
  where f l acc = [  l !! i + max (acc !! i) (acc !! (i + 1)) | i <- [0 .. length l - 1]]

sol :: String -> IO()
sol file = do
  triangle <- readFile file
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  print $ getMaxSum values

